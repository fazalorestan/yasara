"""initial sprint0

Revision ID: 0001_initial_sprint0
Revises:
Create Date: 2026-06-28
"""
from alembic import op

revision = "0001_initial_sprint0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Sprint 0 keeps schema intentionally empty.
    # Sprint 1 will add real market-data tables.
    pass


def downgrade() -> None:
    pass
