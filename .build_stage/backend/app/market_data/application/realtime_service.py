from app.market_data.infrastructure.binance_websocket import binance_ws_manager
from app.market_data.infrastructure.event_bus import market_event_bus

class RealtimeMarketDataService:
    async def start_binance(self, symbols: list[str], timeframes: list[str] | None = None) -> dict:
        selected_tfs = timeframes or ["1m"]
        for symbol in symbols:
            binance_ws_manager.subscribe_ticker(symbol)
            binance_ws_manager.subscribe_depth(symbol)
            for timeframe in selected_tfs:
                binance_ws_manager.subscribe_kline(symbol, timeframe)
        await binance_ws_manager.start()
        return self.stats()

    async def stop_binance(self) -> dict:
        await binance_ws_manager.stop()
        return self.stats()

    def stats(self) -> dict:
        s = binance_ws_manager.stats
        return {
            "websocket": {
                "connected": s.connected,
                "reconnect_count": s.reconnect_count,
                "messages_received": s.messages_received,
                "messages_published": s.messages_published,
                "last_message_at": s.last_message_at.isoformat() if s.last_message_at else None,
                "last_error": s.last_error,
                "subscriptions": len(binance_ws_manager.subscriptions),
            },
            "event_bus": market_event_bus.stats(),
        }

realtime_market_data_service = RealtimeMarketDataService()
