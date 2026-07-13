from app.platform_core.strategy_engine.signal_contract import SignalContractService

def test_v500_alpha41_a_signal_valid():
 s=SignalContractService(); assert s.validate(s.signal())['valid'] is True
