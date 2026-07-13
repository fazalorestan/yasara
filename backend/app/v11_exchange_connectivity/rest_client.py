from app.v11_exchange_connectivity.models import ExchangeRequestPlanV11
from app.v11_exchange_connectivity.profiles import ExchangeProfileRegistryV11
from app.v11_exchange_connectivity.safety import ExchangeSafetyGuardV11


class ExchangeRestClientV11:
    def __init__(self, profiles: ExchangeProfileRegistryV11 | None = None, safety: ExchangeSafetyGuardV11 | None = None):
        self.profiles = profiles or ExchangeProfileRegistryV11()
        self.safety = safety or ExchangeSafetyGuardV11()

    def build_request(self, exchange: str, path: str, method: str = "GET", signed: bool = False) -> ExchangeRequestPlanV11:
        allowed = self.safety.assert_request_allowed(signed=signed, method=method)
        if not allowed:
            raise ValueError("Request blocked by YaSara v1.1 exchange safety policy.")
        profile = self.profiles.get(exchange)
        if profile is None:
            raise ValueError(f"Unsupported exchange: {exchange}")
        normalized_path = path if path.startswith("/") else "/" + path
        return ExchangeRequestPlanV11(
            exchange=profile.exchange,
            path=f"{profile.base_url}{normalized_path}",
            method=method.upper(),
            signed=signed,
            read_only=not signed and method.upper() in {"GET", "HEAD"},
        )
