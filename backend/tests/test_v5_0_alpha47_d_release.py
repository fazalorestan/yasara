from app.platform_core.build_dashboard.release_signal_provider import ReleaseSignalProvider

def test_release(): assert ReleaseSignalProvider().signal()['signal']=='green'
