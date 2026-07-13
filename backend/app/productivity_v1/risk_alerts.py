from pydantic import BaseModel

class RiskAlertInputV1(BaseModel):
    risk_score: float
    exposure_percent: float
    daily_loss_percent: float = 0

class RiskAlertResultV1(BaseModel):
    level: str
    warnings: list[str]

class RiskAlertEngineV1:
    def evaluate(self, item: RiskAlertInputV1) -> RiskAlertResultV1:
        warnings = []
        if item.risk_score >= 80:
            warnings.append("risk_score_high")
        if item.exposure_percent >= 70:
            warnings.append("exposure_high")
        if item.daily_loss_percent <= -5:
            warnings.append("daily_loss_limit_warning")
        level = "critical" if len(warnings) >= 2 else "warning" if warnings else "ok"
        return RiskAlertResultV1(level=level, warnings=warnings)
