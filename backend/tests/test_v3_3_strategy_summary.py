from app.v33_strategy_builder.service import StrategyBuilderServiceV33

def test_v33_summary():
    s = StrategyBuilderServiceV33().summary()
    assert s.product_progress_percent == 65
    assert s.remaining_to_professional_product_percent == 35
