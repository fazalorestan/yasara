from app.platform_core.ai_intelligence.context_contract import AIContextContractService

def test_v500_alpha40_a_context(): assert AIContextContractService().context()['memory_scope']=='yasara_owned'
