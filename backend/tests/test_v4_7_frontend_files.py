from pathlib import Path

def test_v47_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "notificationAlerts.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "NotificationAlertsStatus.tsx").exists()
