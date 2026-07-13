class TradeSimulationEngine:
    def simulate(self, symbol: str, signals: list[dict], quantity: float = 1.0):
        trades = []
        entry = None
        for signal in signals:
            if signal["side"] == "buy":
                entry = signal
            elif signal["side"] == "sell" and entry:
                pnl = (float(signal["price"]) - float(entry["price"])) * quantity
                trades.append({"symbol": symbol, "side": "long", "entry_price": entry["price"], "exit_price": signal["price"], "quantity": quantity, "pnl": pnl})
                entry = None
        return {"ready": True, "trades": trades, "execution_allowed": False}

trade_simulation_engine = TradeSimulationEngine()
