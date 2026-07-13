from app.platform_core.ai_intelligence.agent_registry import AIAgentRegistry

def test_v500_alpha40_d_agents(): assert AIAgentRegistry().list_agents()['count']==2
