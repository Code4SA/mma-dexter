"""fulltext-index

Revision ID: 3192831a2967
Revises: 1a1c0f92befd
Create Date: 2015-11-17 09:35:11.818421

"""

# revision identifiers, used by Alembic.
revision = '3192831a2967'
down_revision = '1a1c0f92befd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute("create fulltext index documents_text_ft_ix on documents(text)")


def downgrade():
    op.drop_index('documents_text_ft_ix', 'documents')
