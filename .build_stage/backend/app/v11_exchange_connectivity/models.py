from enum import Enum
from pydantic import BaseModel, Field
from time import time


class ExchangeConnectivityModeV11(str, Enum):
    READ_ONLY = "read_only"
    PAPER_ONLY = "paper_only"
    LIVE_DISABLED = "live_disabled"


class ExchangeConnectivityStateV11(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    OFFLINE = "offline"
    RATE_LIMITED = "rate_limited"


class ExchangeEndpointProfileV11(BaseModel):
    exchange: str
    base_url: str
    ws_url: str | None = None
    mode: ExchangeConnectivityModeV11 = ExchangeConnectivityModeV11.READ_ONLY
    enabled: bool = True


class ExchangeConnectivityHealthV11(BaseModel):
    exchange: str
    state: ExchangeConnectivityStateV11
    latency_ms: float | None = None
    last_checked: float = Field(default_factory=time)
    message: str = ""


class ExchangeRequestPlanV11(BaseModel):
    exchange: str
    path: str
    method: str = "GET"
    signed: bool = False
    read_only: bool = True


class ExchangeFailoverResultV11(BaseModel):
    selected_exchange: str
    fallback_used: bool = False
    candidates: list[str] = Field(default_factory=list)


class ExchangeConnectivitySummaryV11(BaseModel):
    ready: bool
    mode: ExchangeConnectivityModeV11 = ExchangeConnectivityModeV11.READ_ONLY
    exchanges: list[str] = Field(default_factory=list)
    live_trading_enabled: bool = False
