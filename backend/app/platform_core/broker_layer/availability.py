from app.platform_core.broker_layer.heartbeat import broker_heartbeat_monitor
from app.platform_core.broker_layer.latency import broker_latency_monitor
class BrokerAvailabilityService:
    def availability(self, broker_id: str = "paper.demo"):
        heartbeat = broker_heartbeat_monitor.heartbeat(broker_id)
        latency = broker_latency_monitor.ping(broker_id)
        return {"ready": True, "broker_id": broker_id, "available": heartbeat["alive"] and latency["ready"], "heartbeat": heartbeat, "latency": latency, "real_connection": False, "execution_allowed": False}
broker_availability_service = BrokerAvailabilityService()
