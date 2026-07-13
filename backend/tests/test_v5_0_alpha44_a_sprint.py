from app.platform_core.project_intelligence.sprint_state import SprintStateRegistry

def test_sprint(): assert SprintStateRegistry().snapshot()['current_sprint']=='v5.0-alpha.44'
