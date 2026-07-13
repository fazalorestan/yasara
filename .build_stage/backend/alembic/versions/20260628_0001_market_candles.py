"""create market candles table

Revision ID: 20260628_0001
Revises:
Create Date: 2026-06-28
"""
from alembic import op
import sqlalchemy as sa

revision = "20260628_0001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        "market_candles",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("exchange", sa.String(length=40), nullable=False),
        sa.Column("symbol", sa.String(length=40), nullable=False),
        sa.Column("timeframe", sa.String(length=10), nullable=False),
        sa.Column("open_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("close_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("open", sa.Float(), nullable=False),
        sa.Column("high", sa.Float(), nullable=False),
        sa.Column("low", sa.Float(), nullable=False),
        sa.Column("close", sa.Float(), nullable=False),
        sa.Column("volume", sa.Float(), nullable=False),
        sa.Column("quote_volume", sa.Float(), nullable=False, server_default="0"),
        sa.Column("trades", sa.Integer(), nullable=False, server_default="0"),
        sa.UniqueConstraint("exchange", "symbol", "timeframe", "open_time", name="uq_market_candle"),
    )
    op.create_index("ix_market_candles_exchange", "market_candles", ["exchange"])
    op.create_index("ix_market_candles_symbol", "market_candles", ["symbol"])
    op.create_index("ix_market_candles_timeframe", "market_candles", ["timeframe"])
    op.create_index("ix_market_candles_open_time", "market_candles", ["open_time"])

def downgrade() -> None:
    op.drop_index("ix_market_candles_open_time", table_name="market_candles")
    op.drop_index("ix_market_candles_timeframe", table_name="market_candles")
    op.drop_index("ix_market_candles_symbol", table_name="market_candles")
    op.drop_index("ix_market_candles_exchange", table_name="market_candles")
    op.drop_table("market_candles")
