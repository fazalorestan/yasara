from app.platform_core.project_intelligence.sprint_state_writer import SprintStateWriter

def test_sprint_writer(): assert SprintStateWriter().write_sprint_state()['current_sprint']=='v5.0-alpha.44'
