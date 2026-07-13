from app.v500_alpha1_indicator_expansion.service import IndicatorExpansionFacadeV500Alpha1

def test_v500_alpha1_facade():
 f=IndicatorExpansionFacadeV500Alpha1(); assert f.summary().ready and f.readiness()['yasara_ready'] is True
