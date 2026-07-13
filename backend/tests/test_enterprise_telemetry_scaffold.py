from app.enterprise_v1.telemetry_scaffold import TelemetryEventV1, TelemetryScaffoldV1

def test_telemetry_disabled_by_default():
    telemetry = TelemetryScaffoldV1()
    assert telemetry.track(TelemetryEventV1(name="x")) is False
