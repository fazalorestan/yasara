from app.platform_core.production_runtime.event_bus_contract import RuntimeEventBusContractService

def test_event_bus(): assert RuntimeEventBusContractService().contract()['external_broker_required'] is False
