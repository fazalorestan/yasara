from app.platform_core.broker.validation import broker_order_validator

class BrokerExecutionGuard:
    def check(self, payload: dict):
        validation = broker_order_validator.validate(payload)
        return {"ready": validation["valid"], "validation": validation, "execution_allowed": False, "reason": "live_execution_disabled_by_policy"}
broker_execution_guard = BrokerExecutionGuard()
