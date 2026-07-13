from app.platform_core.execution_engine.fill_contract import FillContractService

def test_v500_alpha42_c_simulated_fill(): assert FillContractService().simulated_fill()['filled'] is False
