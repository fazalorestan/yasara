from app.v500_alpha1_indicator_expansion.models import IndicatorExpansionSummaryV500Alpha1

def test_v500_alpha1_summary():
 s=IndicatorExpansionSummaryV500Alpha1(); assert s.ready and s.default_indicator=='yasara' and s.live_execution_enabled is False
