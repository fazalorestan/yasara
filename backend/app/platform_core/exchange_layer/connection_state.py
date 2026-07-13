class ExchangeConnectionStateMachine:
    def initial(self):
        return {"ready": True, "state": "disconnected"}

    def transition(self, state: str, event: str):
        table = {
            ("disconnected", "connect"): "connecting",
            ("connecting", "connected"): "connected",
            ("connected", "disconnect"): "disconnected",
            ("connected", "stream_timeout"): "degraded",
            ("degraded", "reconnect"): "connecting",
        }
        return {"ready": True, "from": state, "event": event, "to": table.get((state, event), state), "execution_allowed": False}

exchange_connection_state_machine = ExchangeConnectionStateMachine()
