from app.platform_core.exchanges.capabilities import exchange_capability_matrix
from app.platform_core.exchanges.sdk.lifecycle import exchange_connector_lifecycle

class BaseExchangeConnector:
    sdk_version = "1.0"
    minimum_kernel = "5.0"
    maximum_kernel = "5.x"

    def __init__(self, exchange_id: str):
        self.exchange_id = exchange_id
        self.state = exchange_connector_lifecycle.DISCOVERED
        self.last_error = None

    def initialize(self):
        self.state = exchange_connector_lifecycle.INITIALIZED
        return self.status()

    def connect(self):
        self.state = exchange_connector_lifecycle.CONNECTED
        return self.status()

    def disconnect(self):
        self.state = exchange_connector_lifecycle.DISCONNECTED
        return self.status()

    def authenticate(self):
        return {"ready": True, "exchange_id": self.exchange_id, "authenticated": False, "mode": "contract_only"}

    def heartbeat(self):
        return {"ready": True, "exchange_id": self.exchange_id, "state": self.state, "latency_ms": 0}

    def reconnect(self):
        self.state = exchange_connector_lifecycle.RECOVERING
        self.state = exchange_connector_lifecycle.READY
        return self.status()

    def shutdown(self):
        self.state = exchange_connector_lifecycle.SHUTDOWN
        return self.status()

    def diagnostics(self):
        return {"ready": True, "exchange_id": self.exchange_id, "state": self.state, "last_error": self.last_error}

    def capabilities(self):
        return exchange_capability_matrix.get(self.exchange_id)

    def status(self):
        return {"ready": True, "exchange_id": self.exchange_id, "state": self.state, "real_connection": False, "execution_allowed": False}
