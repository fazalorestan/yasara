from app.platform_core.backtest_engine.dataset import historical_dataset_contract

class ReplayTimelineService:
    def build(self):
        data = historical_dataset_contract.sample()
        events = []
        for index, candle in enumerate(data["candles"]):
            events.append({"index": index, "event_type": "candle", "payload": candle, "timestamp": candle["timestamp"]})
        return {"ready": True, "symbol": data["symbol"], "timeframe": data["timeframe"], "events": events, "total_events": len(events)}

replay_timeline_service = ReplayTimelineService()
