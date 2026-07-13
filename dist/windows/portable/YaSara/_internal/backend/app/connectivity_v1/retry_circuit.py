from enum import StrEnum
from pydantic import BaseModel

class CircuitState(StrEnum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class RetryPolicyV1(BaseModel):
    max_attempts: int = 3
    base_delay_seconds: float = 0.5

    def delay_for_attempt(self, attempt: int) -> float:
        return self.base_delay_seconds * (2 ** max(0, attempt - 1))

class CircuitBreakerV1:
    def __init__(self, failure_threshold: int = 3):
        self.failure_threshold = failure_threshold
        self.failures = 0
        self.state = CircuitState.CLOSED

    def record_success(self):
        self.failures = 0
        self.state = CircuitState.CLOSED
        return self.state

    def record_failure(self):
        self.failures += 1
        if self.failures >= self.failure_threshold:
            self.state = CircuitState.OPEN
        return self.state

    def allow_request(self) -> bool:
        return self.state != CircuitState.OPEN
