from app.platform_core.windows_packaging_enablement.real_build_gate import WindowsRealBuildGate

def test_gate(): assert WindowsRealBuildGate().gate()['blocks_broker_connection'] is True
