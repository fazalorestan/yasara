import uuid
from app.execution_v1.domain.models import ExecutionIntent, ExecutionIntentStatus, ExecutionMode, ExecutionResult
from app.execution_v1.engine.audit import ExecutionAuditLogV1
from app.execution_v1.engine.safety_gate import ExecutionSafetyGateV1
from app.execution_v1.infrastructure.dry_run_executor import DryRunExecutorV1

class ExecutionGatewayV1:
    def __init__(self):
        self.safety_gate = ExecutionSafetyGateV1()
        self.audit = ExecutionAuditLogV1()
        self.dry_run_executor = DryRunExecutorV1()

    async def execute(self, intent: ExecutionIntent) -> ExecutionResult:
        self.audit.record("intent_received", "Execution intent received.", intent=intent)
        safety = self.safety_gate.validate(intent)
        if not safety.passed:
            result = ExecutionResult(
                execution_id=uuid.uuid4().hex,
                intent=intent,
                status=ExecutionIntentStatus.REJECTED,
                safety=safety,
                message="Execution rejected by safety gate.",
            )
            self.audit.record("execution_rejected", result.message, intent=intent, result=result)
            return result

        if intent.mode == ExecutionMode.DRY_RUN:
            result = await self.dry_run_executor.execute(intent)
            result.safety = safety
            self.audit.record("dry_run_executed", result.message, intent=intent, result=result)
            return result

        if intent.mode == ExecutionMode.PAPER:
            result = ExecutionResult(
                execution_id=uuid.uuid4().hex,
                intent=intent,
                status=ExecutionIntentStatus.APPROVED,
                safety=safety,
                message="Paper execution handoff approved. Use Paper Trading API for stateful simulation.",
            )
            self.audit.record("paper_handoff_approved", result.message, intent=intent, result=result)
            return result

        result = ExecutionResult(
            execution_id=uuid.uuid4().hex,
            intent=intent,
            status=ExecutionIntentStatus.REJECTED,
            safety=safety,
            message="Unsupported execution mode.",
        )
        self.audit.record("execution_rejected", result.message, intent=intent, result=result)
        return result
