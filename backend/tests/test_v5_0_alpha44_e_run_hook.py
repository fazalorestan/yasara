from app.platform_core.project_intelligence.run_hook_contract import RunHookContractService

def test_run_hook(): assert RunHookContractService().hook()['enabled'] is True
