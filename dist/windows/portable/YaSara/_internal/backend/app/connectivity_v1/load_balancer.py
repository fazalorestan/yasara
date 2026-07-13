from pydantic import BaseModel

class ExchangeLoadCandidateV1(BaseModel):
    name: str
    healthy: bool = True
    latency_ms: float = 0
    current_load: float = 0

class ExchangeLoadBalancerV1:
    def choose(self, candidates: list[ExchangeLoadCandidateV1]) -> ExchangeLoadCandidateV1 | None:
        healthy = [c for c in candidates if c.healthy]
        if not healthy:
            return None
        return sorted(healthy, key=lambda c: (c.current_load, c.latency_ms))[0]
