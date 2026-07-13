from app.platform_core.indicators.v5_expansion.generic_contract import GenericIndicatorContractService

def test_v500_alpha1_generic_contract():
 c=GenericIndicatorContractService().contract(); assert c['ready'] is True and 'direct_live_execution' in c['forbidden']
