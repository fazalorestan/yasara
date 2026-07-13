from app.platform_core.ai_intelligence.tool_safety import AIToolSafetyPolicy

def test_v500_alpha40_c_tool_safety(): assert AIToolSafetyPolicy().policy()['financial_action_allowed'] is False
