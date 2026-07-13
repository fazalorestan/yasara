from app.platform_core.ai_intelligence.provider_registry import AIProviderRegistry

def test_v500_alpha40_a_provider_get(): assert AIProviderRegistry().get('sim.local')['ready'] is True
