class BrokerConnectionStateMachine:
    def initial(self): return {"ready": True, "state": "disconnected"}
    def transition(self, state: str, event: str):
        table = {("disconnected","connect"):"connecting", ("connecting","connected"):"connected", ("connected","disconnect"):"disconnected", ("connected","heartbeat_timeout"):"degraded", ("degraded","reconnect"):"connecting"}
        return {"ready": True, "from": state, "event": event, "to": table.get((state,event), state), "execution_allowed": False}
broker_connection_state_machine = BrokerConnectionStateMachine()
