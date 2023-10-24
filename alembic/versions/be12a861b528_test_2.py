"""Test 2

Revision ID: be12a861b528
Revises: a7295b0389b5
Create Date: 2023-10-23 23:10:24.744155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be12a861b528'
down_revision: Union[str, None] = 'a7295b0389b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(), nullable=True),
    sa.Column('short_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_files_file_name'), 'files', ['file_name'], unique=False)
    op.create_index(op.f('ix_files_id'), 'files', ['id'], unique=False)
    op.create_index(op.f('ix_files_short_url'), 'files', ['short_url'], unique=True)
    op.drop_index('ix_urls_id', table_name='urls')
    op.drop_index('ix_urls_original_url', table_name='urls')
    op.drop_index('ix_urls_short_url', table_name='urls')
    op.drop_table('urls')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('original_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('short_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='urls_pkey')
    )
    op.create_index('ix_urls_short_url', 'urls', ['short_url'], unique=False)
    op.create_index('ix_urls_original_url', 'urls', ['original_url'], unique=False)
    op.create_index('ix_urls_id', 'urls', ['id'], unique=False)
    op.drop_index(op.f('ix_files_short_url'), table_name='files')
    op.drop_index(op.f('ix_files_id'), table_name='files')
    op.drop_index(op.f('ix_files_file_name'), table_name='files')
    op.drop_table('files')
    # ### end Alembic commands ###
