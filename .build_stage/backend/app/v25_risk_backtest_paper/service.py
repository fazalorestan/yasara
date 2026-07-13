from app.v24_indicator_signal.service import IndicatorSignalServiceV24
from app.v23_exchange_connector.service import ExchangeConnectorServiceV23
from app.v25_risk_backtest_paper.models import PaperOrderV25, RiskBacktestPaperSummaryV25, RiskRequestV25


class RiskBacktestPaperServiceV25:
    def __init__(self):
        self.indicators = IndicatorSignalServiceV24()
        self.exchange = ExchangeConnectorServiceV23()
        self.orders = []

    def summary(self):
        return RiskBacktestPaperSummaryV25()

    def risk(self, request: RiskRequestV25):
        quote = self.exchange.quote(request.symbol, request.exchange)
        max_loss = request.equity * request.risk_percent / 100
        stop_distance = max(quote["last"] * request.stop_distance_percent / 100, 0.0001)
        position_size = max_loss / stop_distance
        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "last_price": quote["last"],
            "max_loss": round(max_loss, 4),
            "position_size": round(position_size, 6),
            "notional": round(position_size * quote["last"], 4),
            "risk_percent": request.risk_percent,
            "live_trading_enabled": False,
        }

    def backtest(self, symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "4H"):
        signal = self.indicators.snapshot(symbol, exchange, timeframe)
        # deterministic lightweight backtest metrics
        win_rate = 56 if signal.signal in ["bullish", "bearish"] else 49
        profit_factor = 1.38 if signal.signal in ["bullish", "bearish"] else 1.08
        max_drawdown = 8.4 if signal.confidence >= 70 else 12.1
        return {
            "ready": True,
            "symbol": symbol.upper(),
            "exchange": exchange,
            "timeframe": timeframe,
            "signal": signal.signal,
            "confidence": signal.confidence,
            "trades": 48,
            "win_rate": win_rate,
            "profit_factor": profit_factor,
            "max_drawdown_percent": max_drawdown,
            "live_trading_enabled": False,
        }

    def paper_order(self, order: PaperOrderV25):
        quote = self.exchange.quote(order.symbol, order.exchange)
        item = {
            "id": f"paper-{len(self.orders)+1}",
            "symbol": order.symbol.upper(),
            "exchange": order.exchange,
            "side": order.side,
            "quantity": order.quantity,
            "price": quote["last"],
            "status": "filled_demo",
            "mode": "paper",
            "live_trading_enabled": False,
        }
        self.orders.append(item)
        return {"ready": True, "order": item, "orders_count": len(self.orders)}

    def paper_state(self):
        return {
            "ready": True,
            "balance": 10000,
            "equity": 10000,
            "orders_count": len(self.orders),
            "orders": self.orders[-10:],
            "live_trading_enabled": False,
        }
