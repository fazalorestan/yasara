from app.market_data.application.scheduler import MarketDataScheduler, SyncJobConfig

def test_scheduler_job_registration():
    scheduler = MarketDataScheduler()
    job_id = scheduler.add_sync_job(SyncJobConfig(symbol="BTC/USDT", timeframe="15m"), seconds=60)
    stats = scheduler.stats()
    assert job_id.startswith("sync:")
    assert len(stats["jobs"]) == 1
    assert scheduler.remove_job(job_id) is True
    scheduler.stop()
