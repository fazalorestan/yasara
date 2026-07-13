from app.platform_core.execution_engine.pre_trade_checks import PreTradeCheckService

def test_v500_alpha42_b_pre_trade(): assert PreTradeCheckService().run()['passed'] is True
