class BacktestSignalSimulator:
    def generate(self, candles: list[dict]):
        signals = []
        for i, candle in enumerate(candles):
            if i == 0:
                signals.append({"index": i, "side": "buy", "price": candle["close"], "reason": "sample_entry"})
            elif i == len(candles) - 1:
                signals.append({"index": i, "side": "sell", "price": candle["close"], "reason": "sample_exit"})
        return {"ready": True, "signals": signals}

backtest_signal_simulator = BacktestSignalSimulator()
