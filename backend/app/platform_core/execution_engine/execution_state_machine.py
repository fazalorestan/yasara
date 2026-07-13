class ExecutionStateMachine:
    def initial(self):
        return {"ready": True, "state": "created", "execution_allowed": False}

    def transition(self, state: str = "created", event: str = "validate"):
        table = {
            ("created", "validate"): "validated",
            ("validated", "route"): "routed",
            ("routed", "dry_execute"): "dry_executed",
            ("dry_executed", "journal"): "journaled",
            ("routed", "cancel"): "cancelled",
            ("created", "reject"): "rejected",
        }
        return {"ready": True, "from": state, "event": event, "to": table.get((state, event), state), "execution_allowed": False}

execution_state_machine = ExecutionStateMachine()
