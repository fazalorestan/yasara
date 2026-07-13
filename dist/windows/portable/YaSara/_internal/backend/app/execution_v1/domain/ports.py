from abc import ABC, abstractmethod
from app.execution_v1.domain.models import ExecutionIntent, ExecutionResult

class ExecutionExchangePort(ABC):
    @abstractmethod
    async def execute(self, intent: ExecutionIntent) -> ExecutionResult:
        raise NotImplementedError
