from app.platform_core.project_intelligence.build_hook_contract import BuildHookContractService

def test_build_hook(): assert BuildHookContractService().hook()['enabled'] is True
