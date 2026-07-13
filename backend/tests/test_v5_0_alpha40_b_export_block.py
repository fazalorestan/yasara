from app.platform_core.ai_intelligence.memory_safety import AIMemorySafetyPolicy

def test_v500_alpha40_b_export_block(): assert AIMemorySafetyPolicy().can_export()['allowed'] is False
