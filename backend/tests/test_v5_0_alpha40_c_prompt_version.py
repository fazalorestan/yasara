from app.platform_core.ai_intelligence.prompt_versioning import AIPromptVersioningService

def test_v500_alpha40_c_prompt_version(): assert AIPromptVersioningService().version()['version']=='v1'
