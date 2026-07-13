from app.execution_v1.domain.models import ExecutionIntent, ExecutionMode, SafetyGateResult

class ExecutionSafetyGateV1:
    def validate(self, intent: ExecutionIntent) -> SafetyGateResult:
        reasons = []
        warnings = []

        if intent.quantity <= 0:
            reasons.append("Quantity must be positive.")
        if intent.mode == ExecutionMode.LIVE_DISABLED:
            reasons.append("Live execution is disabled in Sprint 10.")
        if intent.mode not in {ExecutionMode.DRY_RUN, ExecutionMode.PAPER}:
            reasons.append("Unsupported execution mode.")
        if intent.order_type == "limit" and intent.price is None:
            reasons.append("Limit order requires price.")
        if intent.stop_loss is None:
            warnings.append("Stop loss is missing.")
        if intent.take_profit is None:
            warnings.append("Take profit is missing.")

        return SafetyGateResult(passed=len(reasons) == 0, reasons=reasons, warnings=warnings)
