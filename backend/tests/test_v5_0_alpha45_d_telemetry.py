from app.platform_core.production_runtime.telemetry_contract import RuntimeTelemetryContractService

def test_telemetry(): assert RuntimeTelemetryContractService().contract()['external_telemetry_enabled'] is False
