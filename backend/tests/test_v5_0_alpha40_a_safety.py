from app.platform_core.ai_intelligence.safety import AISafetyPolicy

def test_v500_alpha40_a_safety(): assert AISafetyPolicy().policy()['financial_action_allowed'] is False
