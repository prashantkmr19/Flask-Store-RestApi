"""empty message

Revision ID: 754d36098a62
Revises: 634e844407bf
Create Date: 2022-11-24 15:35:58.070002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '754d36098a62'
down_revision = '634e844407bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###