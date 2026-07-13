from pydantic import BaseModel, Field
from app.connectivity_v1.stream_manager import MultiStreamManagerV1, StreamSubscriptionV1, StreamType

class UnifiedStreamRequestV1(BaseModel):
    exchange: str
    symbols: list[str]
    stream_type: StreamType

class UnifiedStreamingAPIServiceV1:
    def __init__(self):
        self.manager = MultiStreamManagerV1()

    def subscribe_many(self, request: UnifiedStreamRequestV1) -> list[StreamSubscriptionV1]:
        result = []
        for symbol in request.symbols:
            stream_id = f"{request.exchange}:{symbol}:{request.stream_type}"
            result.append(self.manager.subscribe(StreamSubscriptionV1(
                stream_id=stream_id,
                exchange=request.exchange,
                symbol=symbol,
                stream_type=request.stream_type,
            )))
        return result
