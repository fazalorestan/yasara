from app.platform_core.ai_intelligence.prompt_registry import AIPromptRegistry

def test_v500_alpha40_c_prompt_get(): assert AIPromptRegistry().get('analysis.default')['ready'] is True
