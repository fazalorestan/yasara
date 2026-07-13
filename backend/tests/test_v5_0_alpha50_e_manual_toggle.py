from app.platform_core.release_candidate.manual_trading_toggle import ManualAutoTradingToggleContract

def test_manual_toggle():
 c=ManualAutoTradingToggleContract().contract(); assert c['user_can_enable'] is True and c['system_can_enable_automatically'] is False
