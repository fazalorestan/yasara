from app.platform_core.execution_engine.fill_contract import FillContractService

def test_v500_alpha42_c_fill_contract(): assert FillContractService().contract()['real_fill_enabled'] is False
