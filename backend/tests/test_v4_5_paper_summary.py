from app.v45_paper_trading.service import PaperTradingExecutionServiceV45

def test_v45_summary():
    s = PaperTradingExecutionServiceV45().summary()
    assert s.product_progress_percent == 96
    assert s.constitution_compliant is True
