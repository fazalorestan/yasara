from pydantic import BaseModel, Field

class IncidentResponseStepV1(BaseModel):
    order: int
    action: str

class IncidentPlanV1(BaseModel):
    incident_type: str
    steps: list[IncidentResponseStepV1] = Field(default_factory=list)

class IncidentPlanBuilderV1:
    def backend_incident(self) -> IncidentPlanV1:
        return IncidentPlanV1(incident_type="backend_incident", steps=[
            IncidentResponseStepV1(order=1, action="capture_logs"),
            IncidentResponseStepV1(order=2, action="stop_backend"),
            IncidentResponseStepV1(order=3, action="run_tests"),
            IncidentResponseStepV1(order=4, action="restore_last_known_good_config"),
            IncidentResponseStepV1(order=5, action="restart_backend"),
        ])
