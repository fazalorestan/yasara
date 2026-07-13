from app.platform_core.ai_decision.consensus import AIConsensusEngine

def test_v500_alpha33_b_consensus_agreement(): assert AIConsensusEngine().consensus([{'direction':'long','weight':1}])['agreement_pct']==100
