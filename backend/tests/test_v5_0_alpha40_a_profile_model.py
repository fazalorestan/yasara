from app.platform_core.ai_intelligence.models import AIProviderProfile

def test_v500_alpha40_a_profile_model(): assert AIProviderProfile('p','Provider').mode=='simulated'
