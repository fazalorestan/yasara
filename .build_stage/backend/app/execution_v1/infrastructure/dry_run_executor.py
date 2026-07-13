import uuid
from app.execution_v1.domain.models import ExecutionIntent, ExecutionIntentStatus, ExecutionResult, SafetyGateResult
from app.execution_v1.domain.ports import ExecutionExchangePort

class DryRunExecutorV1(ExecutionExchangePort):
    async def execute(self, intent: ExecutionIntent) -> ExecutionResult:
        return ExecutionResult(
            execution_id=uuid.uuid4().hex,
            intent=intent,
            status=ExecutionIntentStatus.EXECUTED,
            safety=SafetyGateResult(passed=True),
            exchange_order_id=f"dryrun_{uuid.uuid4().hex}",
            filled_quantity=intent.quantity,
            average_price=intent.price,
            message="Dry-run execution accepted. No live exchange order was sent.",
        )
