from app.platform_core.ai_intelligence.agent_runtime import AIAgentRuntimeContract

def test_v500_alpha40_d_runtime_contract(): assert AIAgentRuntimeContract().contract()['agent_execution_enabled'] is False
