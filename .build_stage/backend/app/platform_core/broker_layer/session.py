class BrokerSessionManager:
    def create_session(self, broker_id: str = "paper.demo"):
        return {"ready": True, "session_id": f"session::{broker_id}", "broker_id": broker_id, "state": "created", "real_connection": False, "execution_allowed": False}
    def close_session(self, session_id: str):
        return {"ready": True, "session_id": session_id, "state": "closed", "execution_allowed": False}
broker_session_manager = BrokerSessionManager()
