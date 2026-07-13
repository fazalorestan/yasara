from app.platform_core.production_readiness.production_contract import ProductionReadinessContract

def test_contract(): assert ProductionReadinessContract().contract()['windows_exe_handoff_ready'] is True
