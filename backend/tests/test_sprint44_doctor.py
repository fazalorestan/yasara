from app.v52_ai_decision_engine.service import ai_decision_facade
def test_doctor(): assert ai_decision_facade.doctor()["ready"] is True
