from app.platform_core.indicators.v5_expansion.capability_matrix import IndicatorCapabilityMatrixService

def test_v500_alpha1_capability_matrix():
 m=IndicatorCapabilityMatrixService().matrix(); assert m['ready'] and any(r['indicator']=='yasara' and r['runtime'] for r in m['rows'])
