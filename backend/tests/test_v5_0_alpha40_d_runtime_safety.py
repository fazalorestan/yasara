from app.platform_core.ai_intelligence.runtime_safety import AIAgentRuntimeSafety

def test_v500_alpha40_d_runtime_safety(): assert AIAgentRuntimeSafety().policy()['agent_execution_enabled'] is False
