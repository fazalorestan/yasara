from pydantic import BaseModel, Field

class ConnectivityPhaseSummaryV1(BaseModel):
    phase: str = "connectivity_phase_1"
    modules: list[str] = Field(default_factory=list)
    ready: bool = True

class ConnectivityPhaseSummaryBuilderV1:
    def build(self) -> ConnectivityPhaseSummaryV1:
        return ConnectivityPhaseSummaryV1(modules=[
            "websocket_core",
            "stream_manager",
            "rate_limiter",
            "retry_circuit",
            "latency_monitor",
            "synchronizer",
            "balance_sync",
            "historical_cache",
            "data_integrity",
            "failover_pro",
            "load_balancer",
            "unified_streaming",
        ])
