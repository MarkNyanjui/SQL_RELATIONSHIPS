"""initial Migration

Revision ID: 418404624ede
Revises: 
Create Date: 2024-09-12 10:26:31.647184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '418404624ede'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('student_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.String(length=6), nullable=True),
    sa.Column('dob', sa.String(length=8), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_table('profile',
    sa.Column('profile_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('admin_no', sa.Integer(), nullable=True),
    sa.Column('class_name', sa.String(length=100), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('profile_id'),
    sa.UniqueConstraint('student_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    op.drop_table('students')
    # ### end Alembic commands ###
