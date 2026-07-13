from app.platform_core.project_intelligence.module_state import ModuleStateRegistry

def test_module(): assert 'Project Intelligence Center' in ModuleStateRegistry().snapshot()['active_modules']
