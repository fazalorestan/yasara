from app.platform_core.ai_intelligence.prompt_contract import AIPromptContractService

def test_v500_alpha40_a_prompt(): assert AIPromptContractService().prompt()['ready'] is True
