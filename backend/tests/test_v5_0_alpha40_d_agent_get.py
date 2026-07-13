from app.platform_core.ai_intelligence.agent_registry import AIAgentRegistry

def test_v500_alpha40_d_agent_get(): assert AIAgentRegistry().get('analyst.agent')['ready'] is True
