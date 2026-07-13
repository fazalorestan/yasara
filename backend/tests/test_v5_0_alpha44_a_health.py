from app.platform_core.project_intelligence.health_state import ProjectHealthStateRegistry

def test_health(): assert ProjectHealthStateRegistry().snapshot()['project_health']=='green'
