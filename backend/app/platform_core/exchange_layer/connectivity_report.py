from app.platform_core.exchange_layer.connection_state import exchange_connection_state_machine
from app.platform_core.exchange_layer.heartbeat import exchange_heartbeat_monitor
from app.platform_core.exchange_layer.latency import exchange_latency_monitor
from app.platform_core.exchange_layer.session import exchange_session_manager
from app.platform_core.exchange_layer.streams import exchange_stream_contract_service
from app.platform_core.exchange_layer.websocket_simulation import exchange_websocket_simulation_service

class ExchangeConnectivityReportService:
    def report(self):
        return {
            "ready": True,
            "session": exchange_session_manager.create_session(),
            "state": exchange_connection_state_machine.transition("disconnected", "connect"),
            "heartbeat": exchange_heartbeat_monitor.heartbeat(),
            "latency": exchange_latency_monitor.ping(),
            "stream_contract": exchange_stream_contract_service.stream_contract(),
            "stream_preview": exchange_stream_contract_service.subscribe_preview(),
            "websocket_simulation": exchange_websocket_simulation_service.simulated_event(),
            "real_exchange_connection": False,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

exchange_connectivity_report_service = ExchangeConnectivityReportService()
