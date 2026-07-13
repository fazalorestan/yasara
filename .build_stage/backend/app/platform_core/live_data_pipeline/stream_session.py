class LiveStreamSessionManager:
    def create(self, provider_id: str = "sim.exchange"):
        return {"ready": True, "session_id": f"stream-session::{provider_id}", "provider_id": provider_id, "state": "created", "real_connection": False, "execution_allowed": False}
    def close(self, session_id: str):
        return {"ready": True, "session_id": session_id, "state": "closed", "execution_allowed": False}
live_stream_session_manager = LiveStreamSessionManager()
