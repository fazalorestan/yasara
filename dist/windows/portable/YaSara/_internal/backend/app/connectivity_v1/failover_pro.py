from pydantic import BaseModel

class FailoverCandidateV1(BaseModel):
    name: str
    healthy: bool = True
    latency_ms: float = 0

class FailoverProDecisionV1(BaseModel):
    selected: str | None
    reason: str

class FailoverProEngineV1:
    def choose(self, candidates: list[FailoverCandidateV1]) -> FailoverProDecisionV1:
        healthy = [c for c in candidates if c.healthy]
        if not healthy:
            return FailoverProDecisionV1(selected=None, reason="no_healthy_candidate")
        selected = sorted(healthy, key=lambda c: c.latency_ms)[0]
        return FailoverProDecisionV1(selected=selected.name, reason="lowest_latency_healthy_candidate")
