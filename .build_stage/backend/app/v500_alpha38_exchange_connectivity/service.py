from app.platform_core.exchange_layer.connection_state import exchange_connection_state_machine
from app.platform_core.exchange_layer.connectivity_readiness import exchange_connectivity_readiness_gate
from app.platform_core.exchange_layer.connectivity_report import exchange_connectivity_report_service
from app.platform_core.exchange_layer.heartbeat import exchange_heartbeat_monitor
from app.platform_core.exchange_layer.latency import exchange_latency_monitor
from app.platform_core.exchange_layer.session import exchange_session_manager
from app.platform_core.exchange_layer.streams import exchange_stream_contract_service
from app.platform_core.exchange_layer.websocket_simulation import exchange_websocket_simulation_service
from app.v500_alpha38_exchange_connectivity.models import ExchangeConnectivitySummaryV500Alpha38

class ExchangeConnectivityFacadeV500Alpha38:
    def summary(self): return ExchangeConnectivitySummaryV500Alpha38()
    def session(self): return exchange_session_manager.create_session()
    def close_session(self): return exchange_session_manager.close_session("exchange-session::binance.sandbox")
    def connection_state(self): return exchange_connection_state_machine.transition("disconnected", "connect")
    def heartbeat(self): return exchange_heartbeat_monitor.heartbeat()
    def timeout_check(self): return exchange_heartbeat_monitor.timeout_check(0)
    def latency(self): return exchange_latency_monitor.ping()
    def latency_grade(self): return exchange_latency_monitor.latency_grade(0)
    def stream_contract(self): return exchange_stream_contract_service.stream_contract()
    def subscribe_preview(self): return exchange_stream_contract_service.subscribe_preview()
    def websocket_event(self): return exchange_websocket_simulation_service.simulated_event()
    def report(self): return exchange_connectivity_report_service.report()
    def readiness(self): return exchange_connectivity_readiness_gate.run()
    def contract(self): return {"ready": True, "exchange_layer": "package_c_connectivity_streams", "execution_allowed": False}

exchange_connectivity_facade_v500_alpha38 = ExchangeConnectivityFacadeV500Alpha38()
