import time
import uuid
from app.exchange_private_v1.domain.models import ExchangeBalanceSnapshot, ExchangePositionSnapshot, PrivateExchange, PrivateOrderRequest, PrivateOrderResult, PrivateOrderStatus
from app.exchange_private_v1.engine.signer import BinanceRequestSignerV1
from app.exchange_private_v1.engine.safety import PrivateExchangeSafetyGateV1
from app.secrets_v1.application.service import secrets_vault_service_v1

class BinanceFuturesPrivateAdapterV1:
    def __init__(self):
        self.signer = BinanceRequestSignerV1()
        self.safety = PrivateExchangeSafetyGateV1()

    async def place_order(self, request: PrivateOrderRequest) -> PrivateOrderResult:
        errors = self.safety.validate_order(request)
        if errors:
            return PrivateOrderResult(accepted=False, status=PrivateOrderStatus.REJECTED, symbol=request.symbol, side=request.side, quantity=request.quantity, message="; ".join(errors))

        api_key = await secrets_vault_service_v1.resolve_secret(request.credential_ref.owner_id, request.credential_ref.api_key_secret_name)
        api_secret = await secrets_vault_service_v1.resolve_secret(request.credential_ref.owner_id, request.credential_ref.api_secret_secret_name)
        if not api_key or not api_secret:
            return PrivateOrderResult(accepted=False, status=PrivateOrderStatus.REJECTED, symbol=request.symbol, side=request.side, quantity=request.quantity, message="Exchange credentials not found.")

        params = {
            "symbol": request.symbol.replace("/", ""),
            "side": request.side.value,
            "type": request.order_type.value,
            "quantity": request.quantity,
            "timestamp": int(time.time() * 1000),
        }
        if request.price is not None:
            params["price"] = request.price
        if request.reduce_only:
            params["reduceOnly"] = "true"

        signed = self.signer.sign(params, api_secret)
        preview = {k: v for k, v in signed.items() if k != "signature"}
        preview["signature"] = "***redacted***"
        preview["api_key"] = f"{api_key[:4]}***" if len(api_key) >= 4 else "***"

        return PrivateOrderResult(
            accepted=True,
            status=PrivateOrderStatus.ACCEPTED_DRY_RUN,
            exchange=PrivateExchange.BINANCE_FUTURES,
            symbol=request.symbol,
            side=request.side,
            quantity=request.quantity,
            exchange_order_id=f"binance_dryrun_{uuid.uuid4().hex}",
            message="Binance Futures private order prepared in dry-run mode. No live order was sent.",
            signed_payload_preview=preview,
        )

    async def get_balances(self, owner_id: str = "default") -> ExchangeBalanceSnapshot:
        return ExchangeBalanceSnapshot(exchange=PrivateExchange.BINANCE_FUTURES, owner_id=owner_id, balances={"USDT": 10000.0}, dry_run=True)

    async def get_positions(self, owner_id: str = "default") -> ExchangePositionSnapshot:
        return ExchangePositionSnapshot(exchange=PrivateExchange.BINANCE_FUTURES, owner_id=owner_id, positions=[], dry_run=True)
