from app.platform_core.ai_intelligence.safety import AISafetyPolicy

def test_v500_alpha40_a_tool_block(): assert AISafetyPolicy().can_execute_tool()['allowed'] is False
