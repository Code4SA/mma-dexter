"""document_text_full_text

Revision ID: 31d59e7965ee
Revises: 22cca3f625d6
Create Date: 2015-07-02 12:40:50.689708

"""

# revision identifiers, used by Alembic.
revision = '31d59e7965ee'
down_revision = '22cca3f625d6'

from alembic import op


def upgrade():
    op.execute("create fulltext index documents_text_ft_ix on documents(text)")


def downgrade():
    op.drop_index('documents_text_ft_ix', 'documents')
