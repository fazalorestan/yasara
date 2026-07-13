import uuid
from app.account_sync_v1.domain.models import AccountEventType, AccountStreamEvent
from app.exchange_private_v1.domain.models import PrivateExchange

class BinanceUserDataEventNormalizerV1:
    def normalize(self, owner_id: str, payload: dict) -> AccountStreamEvent:
        raw_type = payload.get("e", "")
        event_type = {
            "ACCOUNT_UPDATE": AccountEventType.BALANCE_UPDATE,
            "ORDER_TRADE_UPDATE": AccountEventType.ORDER_UPDATE,
            "ACCOUNT_CONFIG_UPDATE": AccountEventType.ACCOUNT_CONFIG_UPDATE,
        }.get(raw_type, AccountEventType.UNKNOWN)

        if raw_type == "ACCOUNT_UPDATE" and payload.get("a", {}).get("P"):
            event_type = AccountEventType.POSITION_UPDATE

        return AccountStreamEvent(
            event_id=uuid.uuid4().hex,
            owner_id=owner_id,
            exchange=PrivateExchange.BINANCE_FUTURES,
            event_type=event_type,
            payload=payload,
        )
