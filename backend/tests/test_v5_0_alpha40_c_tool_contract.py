from app.platform_core.ai_intelligence.tool_contract import AIToolContractService

def test_v500_alpha40_c_tool_contract(): assert AIToolContractService().contract()['tool_execution_enabled'] is False
