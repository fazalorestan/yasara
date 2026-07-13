from app.platform_core.build_dashboard.build_timeline_provider import BuildTimelineProvider

def test_timeline(): assert BuildTimelineProvider().timeline()['latest_build_id']=='2026.47.C.001'
