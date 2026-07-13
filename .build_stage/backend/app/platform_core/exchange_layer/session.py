class ExchangeSessionManager:
    def create_session(self, exchange_id: str = "binance.sandbox"):
        return {
            "ready": True,
            "session_id": f"exchange-session::{exchange_id}",
            "exchange_id": exchange_id,
            "state": "created",
            "real_connection": False,
            "execution_allowed": False,
        }

    def close_session(self, session_id: str):
        return {"ready": True, "session_id": session_id, "state": "closed", "execution_allowed": False}

exchange_session_manager = ExchangeSessionManager()
