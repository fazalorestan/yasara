from app.platform_core.ai_intelligence.tool_safety import AIToolSafetyPolicy

def test_v500_alpha40_c_can_execute(): assert AIToolSafetyPolicy().can_execute()['allowed'] is False
