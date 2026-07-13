from app.platform_core.live_data_pipeline.event_dispatcher import live_stream_event_dispatcher
from app.platform_core.live_data_pipeline.stream_heartbeat import live_stream_heartbeat
from app.platform_core.live_data_pipeline.stream_metrics import live_stream_metrics_service
from app.platform_core.live_data_pipeline.stream_recovery import live_stream_recovery_policy
from app.platform_core.live_data_pipeline.stream_registry import live_stream_registry
from app.platform_core.live_data_pipeline.stream_session import live_stream_session_manager
from app.platform_core.live_data_pipeline.subscriptions import live_stream_subscription_manager

class LiveStreamManagerReport:
    def report(self):
        return {
            "ready": True,
            "streams": live_stream_registry.list_streams(),
            "subscription": live_stream_subscription_manager.subscribe(),
            "session": live_stream_session_manager.create(),
            "heartbeat": live_stream_heartbeat.ping(),
            "recovery": live_stream_recovery_policy.policy(),
            "dispatcher": live_stream_event_dispatcher.dispatch_preview(),
            "metrics": live_stream_metrics_service.metrics(),
            "real_connection": False,
            "real_websocket": False,
            "execution_allowed": False,
        }
live_stream_manager_report = LiveStreamManagerReport()
