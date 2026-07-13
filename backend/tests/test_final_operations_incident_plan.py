from app.final_operations_v1.incident_plan import IncidentPlanBuilderV1

def test_incident_plan():
    plan = IncidentPlanBuilderV1().backend_incident()
    assert plan.steps[-1].action == "restart_backend"
