"""add hashed password

Revision ID: 49f5a490db99
Revises: 8d45f6b00beb
Create Date: 2022-08-29 21:08:14.309022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "49f5a490db99"
down_revision = "8d45f6b00beb"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("hashed_password", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "hashed_password")
