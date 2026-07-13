from app.platform_core.ai_intelligence.reasoning_trace import AIReasoningTraceContract

def test_v500_alpha40_d_trace(): assert AIReasoningTraceContract().trace()['private_chain_of_thought_exposed'] is False
