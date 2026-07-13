class ExchangeConnectorLifecycle:
    DISCOVERED = "discovered"
    REGISTERED = "registered"
    INITIALIZED = "initialized"
    READY = "ready"
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    FAILED = "failed"
    RECOVERING = "recovering"
    SHUTDOWN = "shutdown"

    def states(self):
        return [
            self.DISCOVERED,
            self.REGISTERED,
            self.INITIALIZED,
            self.READY,
            self.CONNECTED,
            self.DISCONNECTED,
            self.FAILED,
            self.RECOVERING,
            self.SHUTDOWN,
        ]

    def can_transition(self, current: str, target: str):
        allowed = {
            self.DISCOVERED: [self.REGISTERED],
            self.REGISTERED: [self.INITIALIZED, self.SHUTDOWN],
            self.INITIALIZED: [self.READY, self.FAILED],
            self.READY: [self.CONNECTED, self.DISCONNECTED, self.SHUTDOWN],
            self.CONNECTED: [self.DISCONNECTED, self.FAILED],
            self.DISCONNECTED: [self.CONNECTED, self.SHUTDOWN],
            self.FAILED: [self.RECOVERING, self.SHUTDOWN],
            self.RECOVERING: [self.READY, self.FAILED],
            self.SHUTDOWN: [],
        }
        return target in allowed.get(current, [])

exchange_connector_lifecycle = ExchangeConnectorLifecycle()
