from app.platform_core.strategy_engine.signal_contract import SignalContractService

def test_v500_alpha41_a_signal(): assert SignalContractService().signal()['side']=='hold'
