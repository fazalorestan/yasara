from app.platform_core.risk_engine.drawdown import DrawdownGuard

def test_v500_alpha23_drawdown(): assert DrawdownGuard().check(5,10)['allowed'] is True
