from app.platform_core.ai_intelligence.provider_registry import AIProviderRegistry

def test_v500_alpha40_a_providers(): assert AIProviderRegistry().list_providers()['count']==2
