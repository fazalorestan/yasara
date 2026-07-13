from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v42_signal_engine.models import SignalRequestV42
from app.v42_signal_engine.service import MultiLayerSignalEngineServiceV42
from app.v45_paper_trading.engine import PaperExecutionSimulatorV45
from app.v45_paper_trading.models import PaperAccountResetV45, PaperOrderRequestV45, PaperTradingSummaryV45, SignalPaperRequestV45
from app.v45_paper_trading.store import PaperTradingStoreV45


class PaperTradingExecutionServiceV45:
    def __init__(self):
        self.store = PaperTradingStoreV45()
        self.engine = PaperExecutionSimulatorV45()
        self.live = LiveExchangeServiceV31()
        self.signal = MultiLayerSignalEngineServiceV42()

    def summary(self):
        return PaperTradingSummaryV45()

    def account(self):
        data = self.store.read()
        return {"ready": True, "account": data, "real_order_execution_enabled": False, "live_trading_enabled": False}

    def reset(self, request: PaperAccountResetV45):
        return {"ready": True, "account": self.store.reset(request.balance), "real_order_execution_enabled": False}

    def _current_price(self, symbol, exchange):
        quote = self.live.live_tick(symbol=symbol, exchange=exchange)
        return self.engine.mark_price(quote)

    def place_order(self, request: PaperOrderRequestV45):
        account = self.store.read()
        fill_price = request.price if request.order_type == "limit" and request.price else self._current_price(request.symbol, request.exchange)
        account, result = self.engine.place_order(account, request, fill_price)
        account = self.engine.mark_to_market(account, {f"{request.exchange}:{request.symbol.upper()}": fill_price})
        self.store.write(account)
        return {
            "ready": True,
            "result": result,
            "account": account,
            "paper_trading": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def mark_to_market(self):
        account = self.store.read()
        prices = {}
        for p in account["positions"]:
            prices[f"{p['exchange']}:{p['symbol']}"] = self._current_price(p["symbol"], p["exchange"])
        account = self.engine.mark_to_market(account, prices)
        self.store.write(account)
        return {"ready": True, "account": account, "real_order_execution_enabled": False}

    def signal_to_paper(self, request: SignalPaperRequestV45):
        sig = self.signal.generate(SignalRequestV42(
            symbol=request.symbol,
            exchange=request.exchange,
            timeframe=request.timeframe,
            build_type="personal",
            license_key=request.license_key,
            has_exchange_api_key=request.has_exchange_api_key,
            autotrade_checkbox_enabled=request.autotrade_checkbox_enabled,
        ))

        action = sig["signal"]["action"]
        if not request.allow_paper_autotrade or action == "wait":
            return {
                "ready": True,
                "executed": False,
                "reason": "signal_wait_or_paper_autotrade_disabled",
                "signal": sig["signal"],
                "real_order_execution_enabled": False,
            }

        side = "buy" if action == "long" else "sell"
        order = PaperOrderRequestV45(
            symbol=request.symbol,
            exchange=request.exchange,
            side=side,
            quantity=0.01,
            source="signal_engine_v4_2",
        )
        placed = self.place_order(order)
        return {
            "ready": True,
            "executed": placed["result"]["accepted"],
            "signal": sig["signal"],
            "paper_order": placed["result"],
            "account": placed["account"],
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }
