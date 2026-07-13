class ExecutionIdempotencyGuard:
    def key(self, order: dict | None = None):
        order = order or {"symbol": "BTCUSDT", "side": "hold", "quantity": 0.0}
        raw = f"{order.get('symbol')}::{order.get('side')}::{order.get('quantity')}"
        return {"ready": True, "key": raw, "duplicate": False}

    def check(self):
        return {"ready": True, "idempotent": True, "duplicate_detected": False, "execution_allowed": False}

execution_idempotency_guard = ExecutionIdempotencyGuard()
