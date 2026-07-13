import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "data" / "notifications"
ALERTS_FILE = DATA_DIR / "alerts.json"


class NotificationAlertStoreV47:
    def __init__(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if not ALERTS_FILE.exists():
            ALERTS_FILE.write_text(json.dumps({"alerts": [], "rules": []}, indent=2), encoding="utf-8")

    def now(self):
        return datetime.now(timezone.utc).isoformat()

    def read(self):
        return json.loads(ALERTS_FILE.read_text(encoding="utf-8"))

    def write(self, data):
        ALERTS_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        return data

    def add_rule(self, rule):
        data = self.read()
        data["rules"].append(rule.model_dump())
        self.write(data)
        return rule.model_dump()

    def rules(self):
        return self.read().get("rules", [])

    def add_alert(self, alert):
        data = self.read()
        item = alert.model_dump()
        if item["created_at"] == "auto":
            item["created_at"] = self.now()
        data["alerts"].append(item)
        self.write(data)
        return item

    def alerts(self):
        return self.read().get("alerts", [])
