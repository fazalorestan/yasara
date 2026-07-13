from app.platform_core.ai_intelligence.memory_safety import AIMemorySafetyPolicy

def test_v500_alpha40_b_safety(): assert AIMemorySafetyPolicy().policy()['provider_owns_memory'] is False
