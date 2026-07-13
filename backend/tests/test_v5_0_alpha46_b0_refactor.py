from app.platform_core.stabilization.refactor_guard import RefactorGuardService

def test_refactor(): assert RefactorGuardService().policy()['api_breaking_changes_allowed'] is False
