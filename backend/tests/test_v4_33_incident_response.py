from app.platform_core.operations.incident_response import IncidentResponsePlan

def test_v433_incident_response():
    p = IncidentResponsePlan().plan()
    assert p["ready"] is True
    assert "SEV1" in p["severity_levels"]
