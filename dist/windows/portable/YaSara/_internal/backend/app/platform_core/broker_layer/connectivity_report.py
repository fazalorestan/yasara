from app.platform_core.broker_layer.availability import broker_availability_service
from app.platform_core.broker_layer.connection_state import broker_connection_state_machine
from app.platform_core.broker_layer.heartbeat import broker_heartbeat_monitor
from app.platform_core.broker_layer.latency import broker_latency_monitor
from app.platform_core.broker_layer.reconnect import broker_reconnect_policy
from app.platform_core.broker_layer.session import broker_session_manager
class BrokerConnectivityReportService:
    def report(self):
        return {"ready": True, "session": broker_session_manager.create_session(), "state": broker_connection_state_machine.transition("disconnected","connect"), "heartbeat": broker_heartbeat_monitor.heartbeat(), "latency": broker_latency_monitor.ping(), "reconnect": broker_reconnect_policy.policy(), "availability": broker_availability_service.availability(), "real_execution_enabled": False, "auto_trading_enabled": False, "execution_allowed": False}
broker_connectivity_report_service = BrokerConnectivityReportService()
