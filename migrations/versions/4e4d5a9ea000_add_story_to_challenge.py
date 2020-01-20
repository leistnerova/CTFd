"""Add type to awards

Revision ID: 4e4d5a9ea000
Revises: 8369118943a1
Create Date: 2020-01-17 19:37:17.872128

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision = '4e4d5a9ea000'
down_revision = '8369118943a1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('challenges', sa.Column('story', sa.Text, nullable=True))
    op.add_column('challenges', sa.Column('order_priority', sa.Integer, default=0))


def downgrade():
    op.drop_column('challenges', 'story')
    op.drop_column('challenges', 'order_priority')
