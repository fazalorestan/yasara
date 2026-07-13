from app.v500_alpha2_indicator_marketplace.models import IndicatorMarketplaceSummaryV500Alpha2

def test_v500_alpha2_summary():
    s=IndicatorMarketplaceSummaryV500Alpha2(); assert s.ready is True and s.default_indicator=="yasara" and s.live_execution_enabled is False
