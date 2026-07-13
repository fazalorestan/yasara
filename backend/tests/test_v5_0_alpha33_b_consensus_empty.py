from app.platform_core.ai_decision.consensus import AIConsensusEngine

def test_v500_alpha33_b_consensus_empty(): assert AIConsensusEngine().consensus([])['direction']=='neutral'
