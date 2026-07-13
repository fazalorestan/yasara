from app.platform_core.project_intelligence.test_hook_contract import TestHookContractService

def test_test_hook(): assert TestHookContractService().hook()['enabled'] is True
