from pydantic import BaseModel


class ExchangeSafetyPolicyV11(BaseModel):
    live_trading_enabled: bool = False
    allow_signed_requests: bool = False
    allow_private_order_routes: bool = False
    read_only_market_data: bool = True


class ExchangeSafetyGuardV11:
    def __init__(self, policy: ExchangeSafetyPolicyV11 | None = None):
        self.policy = policy or ExchangeSafetyPolicyV11()

    def assert_request_allowed(self, signed: bool, method: str) -> bool:
        if signed and not self.policy.allow_signed_requests:
            return False
        if method.upper() not in {"GET", "HEAD"} and not self.policy.allow_private_order_routes:
            return False
        return True
