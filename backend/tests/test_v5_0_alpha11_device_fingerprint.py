from app.platform_core.licensing.activation.device import DeviceFingerprintContract
def test_v500_alpha11_device_fingerprint():
    r = DeviceFingerprintContract().fingerprint("x")
    assert r["ready"] is True
    assert len(r["fingerprint"]) == 32
