from app.v500_alpha33_ai_decision_core.service import AIDecisionCoreFacadeV500Alpha33

def test_v500_alpha33_a_facade_contract(): assert AIDecisionCoreFacadeV500Alpha33().contract()['execution_allowed'] is False
