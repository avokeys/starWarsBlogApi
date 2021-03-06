"""empty message

Revision ID: 14ac6814c124
Revises: a8a5f3cfc2ce
Create Date: 2022-03-21 22:17:27.695457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14ac6814c124'
down_revision = 'a8a5f3cfc2ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('hair_color', sa.String(length=20), nullable=True))
    op.add_column('people', sa.Column('height', sa.Integer(), nullable=False))
    op.add_column('people', sa.Column('mass', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('people', 'mass')
    op.drop_column('people', 'height')
    op.drop_column('people', 'hair_color')
    # ### end Alembic commands ###
