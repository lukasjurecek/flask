"""empty message

Revision ID: 38f7eed2e67a
Revises: 460d6cc9c9ce
Create Date: 2019-09-30 11:38:34.554421

"""

# revision identifiers, used by Alembic.
revision = '38f7eed2e67a'
down_revision = '460d6cc9c9ce'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sqlite_sequence')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    ### end Alembic commands ###
