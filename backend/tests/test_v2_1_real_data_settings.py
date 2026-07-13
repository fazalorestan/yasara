from app.v21_real_data.service import RealDataActivationServiceV21
from app.v21_real_data.models import UserSettingsV21

def test_real_data_settings():
    service = RealDataActivationServiceV21()
    settings = service.update_settings(UserSettingsV21(default_exchange="binance"))
    assert settings.live_trading_enabled is False
    assert service.get_settings().default_exchange == "binance"
