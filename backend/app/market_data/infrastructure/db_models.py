from datetime import datetime
from sqlalchemy import DateTime, Float, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
try:
    from app.core.database import Base
except Exception:
    from sqlalchemy.orm import declarative_base
    Base = declarative_base()

class MarketCandleORM(Base):
    __tablename__ = "market_candles"
    __table_args__ = (UniqueConstraint("exchange", "symbol", "timeframe", "open_time", name="uq_market_candle"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    exchange: Mapped[str] = mapped_column(String(40), index=True)
    symbol: Mapped[str] = mapped_column(String(40), index=True)
    timeframe: Mapped[str] = mapped_column(String(10), index=True)
    open_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    close_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    open: Mapped[float] = mapped_column(Float)
    high: Mapped[float] = mapped_column(Float)
    low: Mapped[float] = mapped_column(Float)
    close: Mapped[float] = mapped_column(Float)
    volume: Mapped[float] = mapped_column(Float)
    quote_volume: Mapped[float] = mapped_column(Float, default=0)
    trades: Mapped[int] = mapped_column(Integer, default=0)
