from app.platform_core.ai_intelligence.decision_graph import AIDecisionGraphService

def test_v500_alpha40_d_graph(): assert len(AIDecisionGraphService().graph()['nodes']) == 4
