"""add genre model

Revision ID: 5e1dd0790bb6
Revises: 5d075e1b2f68
Create Date: 2022-03-28 21:34:31.490855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e1dd0790bb6'
down_revision = '5d075e1b2f68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_genre',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'genre_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_genre')
    # ### end Alembic commands ###