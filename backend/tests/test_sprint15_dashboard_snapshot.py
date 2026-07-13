import pytest
from app.dashboard_v1.application.service import DashboardServiceV1

@pytest.mark.asyncio
async def test_dashboard_snapshot_builds():
    snapshot = await DashboardServiceV1().snapshot()
    assert snapshot.system.status == "ok"
    assert len(snapshot.panels) >= 4
    assert len(snapshot.watchlist) >= 1
