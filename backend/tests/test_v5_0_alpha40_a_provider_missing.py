from app.platform_core.ai_intelligence.provider_registry import AIProviderRegistry

def test_v500_alpha40_a_provider_missing(): assert AIProviderRegistry().get('x')['ready'] is False
