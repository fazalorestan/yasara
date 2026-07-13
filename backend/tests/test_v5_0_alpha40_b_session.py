from app.platform_core.ai_intelligence.session_memory import AISessionMemoryService

def test_v500_alpha40_b_session(): assert AISessionMemoryService().session()['provider_owned'] is False
