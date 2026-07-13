import os
import time
from app.production_ai_v1.domain.models import ProductionHealthReport, ProductionMetric

class ProductionMonitoringEngineV1:
    def __init__(self):
        self.started_at = time.monotonic()

    def report(self) -> ProductionHealthReport:
        uptime = time.monotonic() - self.started_at
        metrics = [
            ProductionMetric(key="uptime_seconds", value=round(uptime, 2), unit="s"),
            ProductionMetric(key="process_id", value=os.getpid()),
            ProductionMetric(key="python_runtime", value="available"),
            ProductionMetric(key="live_trading_enabled", value=False),
        ]
        warnings = []
        if uptime < 1:
            warnings.append("Service recently started.")
        return ProductionHealthReport(status="ok", metrics=metrics, warnings=warnings)
