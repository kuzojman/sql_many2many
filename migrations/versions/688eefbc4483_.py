"""empty message

Revision ID: 688eefbc4483
Revises: 
Create Date: 2021-02-27 21:34:20.174071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '688eefbc4483'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mail', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('meals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('picture', sa.String(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('picture'),
    sa.UniqueConstraint('title')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=True),
    sa.Column('summ', sa.Float(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('mail', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('adresses', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('meal_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meal_id'], ['meals.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('orders')
    op.drop_table('meals')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###