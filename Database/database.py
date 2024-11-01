from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_scoped_session, async_sessionmaker
from asyncio import current_task
from utils.settings import SETTINGS

class DbHelper:
    def __init__(self, url, echo: bool):
        self.engine = create_async_engine(url, echo=echo)
        self.session_factory = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession,
            autoflush=False,
            autocommit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.close()

db_helper = DbHelper(SETTINGS.DATABASE_URL, SETTINGS.ECHO)