from app.platform_core.build_dashboard.quality_signal_provider import BuildQualitySignalProvider

def test_quality(): assert BuildQualitySignalProvider().signal()['signal']=='green'
