"""empty message

Revision ID: 9c0bb5988b0c
Revises: 8e8dbfacd707
Create Date: 2025-03-18 14:34:58.005213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c0bb5988b0c'
down_revision: Union[str, None] = '8e8dbfacd707'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Categories', schema=None) as batch_op:
        batch_op.drop_column('type')

    # ### end Alembic commands ###
