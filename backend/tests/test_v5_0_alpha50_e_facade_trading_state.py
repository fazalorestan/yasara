from app.v500_alpha50_release_candidate.service import InternalRCPreparationFacadeV500Alpha50

def test_facade_trading_state(): assert InternalRCPreparationFacadeV500Alpha50().trading_state(False, False)['signal_only_mode'] is True
