from app.platform_core.build_dashboard.ci_signal_provider import CISignalProvider

def test_ci(): assert CISignalProvider().signal()['signal']=='green'
