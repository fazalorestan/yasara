import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "data" / "paper_trading"
ACCOUNT_FILE = DATA_DIR / "account.json"


class PaperTradingStoreV45:
    def __init__(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if not ACCOUNT_FILE.exists():
            self.reset(10000)

    def now(self):
        return datetime.now(timezone.utc).isoformat()

    def read(self):
        return json.loads(ACCOUNT_FILE.read_text(encoding="utf-8"))

    def write(self, data):
        ACCOUNT_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        return data

    def reset(self, balance=10000):
        data = {
            "balance": float(balance),
            "equity": float(balance),
            "realized_pnl": 0.0,
            "unrealized_pnl": 0.0,
            "orders": [],
            "positions": [],
        }
        return self.write(data)
