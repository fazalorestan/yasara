from app.platform_core.ai_decision.consensus import AIConsensusEngine

def test_v500_alpha33_b_consensus_long(): assert AIConsensusEngine().consensus([{'direction':'long','weight':2},{'direction':'short','weight':1}])['direction']=='long'
