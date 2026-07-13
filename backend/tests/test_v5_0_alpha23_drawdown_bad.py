from app.platform_core.risk_engine.drawdown import DrawdownGuard

def test_v500_alpha23_drawdown_bad(): assert DrawdownGuard().check(12,10)['reason']=='max_drawdown_exceeded'
