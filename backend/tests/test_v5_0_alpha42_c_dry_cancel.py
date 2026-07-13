from app.platform_core.execution_engine.cancellation_contract import CancellationContractService

def test_v500_alpha42_c_dry_cancel(): assert CancellationContractService().dry_cancel()['cancelled'] is True
