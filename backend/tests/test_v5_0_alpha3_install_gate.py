from app.platform_core.indicators.sandbox.install_gate import IndicatorInstallSafetyGate

def test_v500_alpha3_install_gate():
    manifest = {"name":"yasara","version":"v1","display_name":"YaSara","capabilities":[],"metadata":{"imports":[]}}
    r = IndicatorInstallSafetyGate().evaluate(manifest)
    assert r["ready"] is True
    assert r["execution_allowed"] is False
