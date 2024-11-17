from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .database import db_helper
from sqlalchemy import select
from utils.settings import SETTINGS

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    username = Column(String(123), index=True)
    full_name = Column(String(123))
    wallet = Column(Integer, default=0)
    referral = Column(String(123), nullable=True)

    offers = relationship('UserOffer', back_populates='user')
    referrals = relationship('UserReferral',
                             back_populates='user',
                             foreign_keys='UserReferral.user_id')
    inviter = relationship('UserReferral',
                           back_populates='offered_user',
                           foreign_keys='UserReferral.offered_user_id')

    @classmethod
    async def get(cls, telegram_id=None, referral=None):
        async_session = db_helper.get_scoped_session()
        async with async_session() as session:
            if telegram_id is not None:
                stmt = select(cls).where(cls.telegram_id == telegram_id)
                result = await session.execute(stmt)
                user = result.scalars().first()
                return user
            elif referral is not None:
                stmt = select(cls).where(cls.referral == referral)
                result = await session.execute(stmt)
                user = result.scalars().first()
                return user

    @classmethod
    async def get_or_create(cls, telegram_id: int, **kwargs):
        async_session = db_helper.get_scoped_session()
        async with async_session() as session:
            stmt = select(cls).where(cls.telegram_id == telegram_id)
            result = await session.execute(stmt)
            user = result.scalars().first()

            if user:
                return user
            elif kwargs:
                new_user = cls(
                    telegram_id=telegram_id,
                    username=kwargs.get('username'),
                    full_name=kwargs.get('full_name')
                )
                session.add(new_user)
                await session.commit()
                await session.refresh(new_user)  # Update with DB defaults
                return new_user
            else:
                return None

    async def update(self, wallet=None, referral=None, fullname=None, username=None):
        async_session = db_helper.get_scoped_session()
        async with async_session() as session:
            stmt = select(User).where(User.id == self.id)
            result = await session.execute(stmt)
            user = result.scalars().first()
            if wallet is not None:
                user.wallet = wallet
            if referral is not None:
                user.referral = referral
            if fullname is not None:
                user.full_name = fullname
            if username is not None:
                user.username = username

            await session.commit()
            await session.refresh(user)


class UserOffer(Base):
    __tablename__ = "user_offers"

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(String(123), nullable=True)
    text = Column(Text, nullable=True)
    user_id = Column(ForeignKey('users.id'))

    user = relationship('User', back_populates='offers')

    @classmethod
    async def create(cls, user, file=None, text=None):
        async_session = db_helper.get_scoped_session()
        async with async_session() as session:
            if file:
                new_offer = cls(
                    user=user,
                    file_id=file,
                )
            elif text:
                new_offer = cls(
                    user=user,
                    text=text
                )
            else:
                new_offer = None

            session.add(new_offer)
            await session.commit()
            await session.refresh(new_offer)
            return new_offer


    @classmethod
    async def filter(cls, user_id):
        async_session = db_helper.get_scoped_session()
        async with async_session() as session:
            stmt = select(cls).where(cls.user_id == user_id)
            result = await session.execute(stmt)
            offers = result.scalars().all()
            return offers


class UserReferral(Base):
    __tablename__ = "user_referrals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey('users.id'))
    offered_user_id = Column(ForeignKey('users.id'))
    point = Column(Integer, default=0)

    user = relationship('User', back_populates='referrals', foreign_keys=[user_id])
    offered_user = relationship('User', uselist=False, back_populates='inviter', foreign_keys=[offered_user_id])

    @classmethod
    async def create(cls, user_id, offered_user_id):
        async_session = db_helper.get_scoped_session()
        async with async_session() as session:
            user_referral = cls(
                user_id=user_id,
                offered_user_id=offered_user_id,
                point=int(SETTINGS.POINT)
            )

            session.add(user_referral)
            await session.commit()
            await session.refresh(user_referral)
            return user_referral

    @classmethod
    async def filter(cls, user_id):
        async_session = db_helper.get_scoped_session()
        async with async_session() as session:
            stmt = select(cls).where(cls.user_id == user_id)
            result = await session.execute(stmt)
            referrals = result.scalars().all()

            return list(referrals)

