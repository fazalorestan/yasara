import json
from pathlib import Path
from app.v21_real_data.models import UserSettingsV21, WatchlistItemV21, WatchlistStateV21

DATA_DIR = Path("data/v21")
SETTINGS_FILE = DATA_DIR / "settings.json"
WATCHLIST_FILE = DATA_DIR / "watchlist.json"

DEFAULT_WATCHLIST = [
    WatchlistItemV21(symbol="BTCUSDT", exchange="binance", favorite=True),
    WatchlistItemV21(symbol="ETHUSDT", exchange="binance", favorite=True),
    WatchlistItemV21(symbol="SOLUSDT", exchange="toobit", favorite=False),
    WatchlistItemV21(symbol="XRPUSDT", exchange="binance", favorite=False),
]

class RealDataStoreV21:
    def __init__(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)

    def load_settings(self):
        if not SETTINGS_FILE.exists():
            self.save_settings(UserSettingsV21())
        return UserSettingsV21(**json.loads(SETTINGS_FILE.read_text(encoding="utf-8")))

    def save_settings(self, settings):
        settings.live_trading_enabled = False
        SETTINGS_FILE.write_text(settings.model_dump_json(indent=2), encoding="utf-8")
        return settings

    def load_watchlist(self):
        if not WATCHLIST_FILE.exists():
            self.save_watchlist(WatchlistStateV21(items=DEFAULT_WATCHLIST))
        return WatchlistStateV21(**json.loads(WATCHLIST_FILE.read_text(encoding="utf-8")))

    def save_watchlist(self, state):
        WATCHLIST_FILE.write_text(state.model_dump_json(indent=2), encoding="utf-8")
        return state

    def add_item(self, item):
        state = self.load_watchlist()
        if not any(x.symbol == item.symbol and x.exchange == item.exchange for x in state.items):
            state.items.append(item)
        return self.save_watchlist(state)

    def remove_item(self, symbol, exchange):
        state = self.load_watchlist()
        state.items = [x for x in state.items if not (x.symbol == symbol and x.exchange == exchange)]
        return self.save_watchlist(state)
