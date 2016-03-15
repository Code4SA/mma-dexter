"""many-to-many source roles to natures

Revision ID: 13781c95ccab
Revises: 3e64188fb918
Create Date: 2016-03-15 13:07:26.769278

"""

# revision identifiers, used by Alembic.
revision = '13781c95ccab'
down_revision = '3e64188fb918'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('analysis_nature_source_roles',
    sa.Column('analysis_nature_id', sa.Integer(), nullable=True),
    sa.Column('source_role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['analysis_nature_id'], ['analysis_natures.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['source_role_id'], ['source_roles.id'], ondelete='CASCADE'))

    op.execute("""
        INSERT INTO analysis_nature_source_roles (analysis_nature_id, source_role_id)
        SELECT analysis_nature_id, id
        FROM source_roles WHERE analysis_nature_id IS NOT NULL
    """)


def downgrade():
    op.drop_table('analysis_nature_source_roles')
