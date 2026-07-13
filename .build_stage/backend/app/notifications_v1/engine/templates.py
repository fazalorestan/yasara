from app.notifications_v1.domain.models import NotificationMessage, NotificationPriority, NotificationType

class NotificationTemplateEngineV1:
    def signal_template(self, symbol: str, direction: str, confidence: float, reasons: list[str] | None = None) -> NotificationMessage:
        reason_text = "\n".join(f"- {r}" for r in (reasons or [])[:5])
        return NotificationMessage(
            notification_type=NotificationType.SIGNAL,
            title=f"YaSara Signal: {symbol} {direction.upper()}",
            body=f"Direction: {direction.upper()}\nConfidence: {confidence:.2f}%\n{reason_text}".strip(),
            priority=NotificationPriority.HIGH if confidence >= 80 else NotificationPriority.NORMAL,
            metadata={"symbol": symbol, "direction": direction, "confidence": confidence},
        )

    def system_template(self, title: str, body: str, critical: bool = False) -> NotificationMessage:
        return NotificationMessage(
            notification_type=NotificationType.SYSTEM,
            title=title,
            body=body,
            priority=NotificationPriority.CRITICAL if critical else NotificationPriority.NORMAL,
        )
