from enum import StrEnum
from pydantic import BaseModel, Field

class ConnectionState(StrEnum):
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    RECONNECTING = "reconnecting"

class WebSocketConnectionConfigV1(BaseModel):
    name: str
    url: str
    heartbeat_seconds: int = 30
    auto_reconnect: bool = True

class WebSocketConnectionStateV1(BaseModel):
    name: str
    state: ConnectionState = ConnectionState.DISCONNECTED
    reconnect_attempts: int = 0
    last_message: dict = Field(default_factory=dict)

class WebSocketConnectionManagerV1:
    def __init__(self, config: WebSocketConnectionConfigV1):
        self.config = config
        self.state = WebSocketConnectionStateV1(name=config.name)

    def mark_connecting(self):
        self.state.state = ConnectionState.CONNECTING
        return self.state

    def mark_connected(self):
        self.state.state = ConnectionState.CONNECTED
        return self.state

    def mark_reconnecting(self):
        self.state.state = ConnectionState.RECONNECTING
        self.state.reconnect_attempts += 1
        return self.state

    def mark_disconnected(self):
        self.state.state = ConnectionState.DISCONNECTED
        return self.state
