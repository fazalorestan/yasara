import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
BACKTEST_DIR = ROOT / "data" / "backtests"
BENCHMARKS = BACKTEST_DIR / "benchmarks.json"


class BacktestBenchmarkStoreV44:
    def __init__(self):
        BACKTEST_DIR.mkdir(parents=True, exist_ok=True)
        if not BENCHMARKS.exists():
            BENCHMARKS.write_text(json.dumps({"benchmarks": []}, indent=2), encoding="utf-8")

    def now(self):
        return datetime.now(timezone.utc).isoformat()

    def read(self):
        return json.loads(BENCHMARKS.read_text(encoding="utf-8"))

    def append_benchmark(self, item):
        data = self.read()
        item["created_at"] = self.now()
        data["benchmarks"].append(item)
        BENCHMARKS.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        return item

    def list_benchmarks(self):
        return self.read().get("benchmarks", [])
