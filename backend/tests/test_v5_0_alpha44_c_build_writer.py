from app.platform_core.project_intelligence.build_state_writer import BuildStateWriter

def test_build_writer(): assert BuildStateWriter().write_build_state()['written'] is True
