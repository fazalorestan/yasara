from app.platform_core.ai_intelligence.tool_registry import AIToolRegistry

def test_v500_alpha40_c_tool_get(): assert AIToolRegistry().get('market.context')['ready'] is True
