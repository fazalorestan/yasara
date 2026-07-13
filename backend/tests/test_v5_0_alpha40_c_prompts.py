from app.platform_core.ai_intelligence.prompt_registry import AIPromptRegistry

def test_v500_alpha40_c_prompts(): assert AIPromptRegistry().list_prompts()['count']==2
