"""empty message

Revision ID: 638b40c73835
Revises: 
Create Date: 2019-12-19 18:28:43.047786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '638b40c73835'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tweet_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('retweets', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tweet_id')
    )
    op.create_index(op.f('ix_tweets_date'), 'tweets', ['date'], unique=False)
    op.create_index(op.f('ix_tweets_likes'), 'tweets', ['likes'], unique=False)
    op.create_index(op.f('ix_tweets_retweets'), 'tweets', ['retweets'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tweets_retweets'), table_name='tweets')
    op.drop_index(op.f('ix_tweets_likes'), table_name='tweets')
    op.drop_index(op.f('ix_tweets_date'), table_name='tweets')
    op.drop_table('tweets')
    # ### end Alembic commands ###