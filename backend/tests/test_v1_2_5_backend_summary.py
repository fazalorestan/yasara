from app.v12_realtime_intelligence.service import RealtimeIntelligenceServiceV12
def test_realtime_summary():
    summary = RealtimeIntelligenceServiceV12().summary()
    assert summary["ready"] is True
    assert summary["project_progress_percent"] == 93
    assert summary["remaining_percent"] == 7
