import json
from pathlib import Path
from app.v33_strategy_builder.models import StrategyDefinitionV33

DATA_DIR = Path("data/v33")
STRATEGIES_FILE = DATA_DIR / "strategies.json"


class StrategyStoreV33:
    def __init__(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if not STRATEGIES_FILE.exists():
            STRATEGIES_FILE.write_text("{}", encoding="utf-8")

    def _read(self):
        return json.loads(STRATEGIES_FILE.read_text(encoding="utf-8"))

    def _write(self, data):
        STRATEGIES_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def list(self):
        return [StrategyDefinitionV33(**item) for item in self._read().values()]

    def get(self, strategy_id: str):
        data = self._read()
        item = data.get(strategy_id)
        return StrategyDefinitionV33(**item) if item else None

    def save(self, strategy: StrategyDefinitionV33):
        strategy.live_trading_enabled = False
        data = self._read()
        data[strategy.strategy_id] = strategy.model_dump()
        self._write(data)
        return strategy

    def archive(self, strategy_id: str):
        strategy = self.get(strategy_id)
        if not strategy:
            return None
        strategy.status = "archived"
        return self.save(strategy)
