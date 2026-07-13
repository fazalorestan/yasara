from app.platform_core.windows_builder.startup_validator import WindowsStartupValidator

def test_startup():
 assert WindowsStartupValidator().validate()['auto_trading_enabled_default'] is False
