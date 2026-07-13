from app.platform_core.execution_engine.cancellation_contract import CancellationContractService

def test_v500_alpha42_c_cancel_contract(): assert CancellationContractService().contract()['real_cancel_enabled'] is False
