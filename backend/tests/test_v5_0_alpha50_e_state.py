from app.platform_core.release_candidate.trading_control_state import TradingControlStateContract

def test_state(): assert TradingControlStateContract().state(True, True)['allow_new_order'] is False
