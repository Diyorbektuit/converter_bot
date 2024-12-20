"""user role

Revision ID: 52661f73c311
Revises: 7d1151e5237b
Create Date: 2024-11-19 15:25:44.306322

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52661f73c311'
down_revision: Union[str, None] = '7d1151e5237b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

user_role_enum = sa.Enum('ADMIN', 'USER', name='userrole')


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    user_role_enum.create(op.get_bind())

    # Add the column with the enum type
    op.add_column('users', sa.Column('role', user_role_enum, nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')

    # Drop the enum type from the database
    user_role_enum.drop(op.get_bind())
    # ### end Alembic commands ###
