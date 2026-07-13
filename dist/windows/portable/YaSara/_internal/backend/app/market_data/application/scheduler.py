from dataclasses import dataclass, field
from datetime import datetime, timezone
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.market_data.domain.models import ExchangeCode

@dataclass
class SyncJobConfig:
    symbol: str
    timeframe: str
    limit: int = 500
    exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES

class MarketDataScheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler(timezone="UTC")
        self.jobs: dict[str, SyncJobConfig] = {}
        self.started_at: datetime | None = None

    def start(self) -> None:
        if not self.scheduler.running:
            self.scheduler.start()
            self.started_at = datetime.now(timezone.utc)

    def stop(self) -> None:
        if self.scheduler.running:
            self.scheduler.shutdown(wait=False)

    def add_sync_job(self, config: SyncJobConfig, seconds: int = 60) -> str:
        self.start()
        job_id = f"sync:{config.exchange.value}:{config.symbol}:{config.timeframe}"
        self.jobs[job_id] = config
        self.scheduler.add_job(
            self._placeholder_job,
            "interval",
            seconds=seconds,
            id=job_id,
            replace_existing=True,
            kwargs={"job_id": job_id},
        )
        return job_id

    async def _placeholder_job(self, job_id: str) -> None:
        # Actual DB-bound sync is triggered from API layer where AsyncSession is available.
        return None

    def remove_job(self, job_id: str) -> bool:
        if job_id not in self.jobs:
            return False
        self.jobs.pop(job_id, None)
        try:
            self.scheduler.remove_job(job_id)
        except Exception:
            pass
        return True

    def stats(self) -> dict:
        return {
            "running": self.scheduler.running,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "jobs": [
                {
                    "id": job_id,
                    "symbol": cfg.symbol,
                    "timeframe": cfg.timeframe,
                    "exchange": cfg.exchange.value,
                    "limit": cfg.limit,
                }
                for job_id, cfg in self.jobs.items()
            ],
        }

market_data_scheduler = MarketDataScheduler()
