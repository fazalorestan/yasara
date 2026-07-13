from app.platform_core.replay_engine.timeline import ReplayTimelineService

def test_v500_alpha30_timeline(): assert ReplayTimelineService().build()['total_events'] == 3
