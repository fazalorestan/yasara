import uuid
from app.production_ai_v1.domain.models import AIInsight, AIInsightSeverity, AIInsightType

class AIInsightEngineV1:
    def explain_signal(self, symbol: str, direction: str, confidence: float, reasons: list[str]) -> AIInsight:
        severity = AIInsightSeverity.INFO if confidence >= 50 else AIInsightSeverity.WARNING
        return AIInsight(
            insight_id=uuid.uuid4().hex,
            insight_type=AIInsightType.MARKET,
            title=f"{symbol} {direction.upper()} decision explanation",
            explanation="; ".join(reasons) if reasons else "No detailed reasons were provided.",
            severity=severity,
            confidence=confidence,
            recommended_actions=[
                "Review multi-timeframe alignment.",
                "Validate risk before execution.",
                "Prefer paper trading until live mode is explicitly enabled.",
            ],
            evidence={"symbol": symbol, "direction": direction, "reasons": reasons},
        )

    def explain_risk(self, risk_score: float, warnings: list[str]) -> AIInsight:
        severity = AIInsightSeverity.CRITICAL if risk_score >= 80 else AIInsightSeverity.WARNING if risk_score >= 50 else AIInsightSeverity.INFO
        return AIInsight(
            insight_id=uuid.uuid4().hex,
            insight_type=AIInsightType.RISK,
            title="Risk analysis explanation",
            explanation="; ".join(warnings) if warnings else "Risk is within configured limits.",
            severity=severity,
            confidence=max(0, min(100, 100 - risk_score)),
            recommended_actions=["Reduce exposure." if risk_score >= 80 else "Continue monitoring risk dashboard."],
            evidence={"risk_score": risk_score, "warnings": warnings},
        )
