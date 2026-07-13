from app.notifications_v1.engine.templates import NotificationTemplateEngineV1

def test_signal_template_priority():
    message = NotificationTemplateEngineV1().signal_template("BTC/USDT", "long", 85.5, ["Trend bullish"])
    assert "BTC/USDT" in message.title
    assert message.priority == "high"
    assert message.metadata["confidence"] == 85.5
