from pydantic import BaseModel

class BrokerMonitoringSummaryV500Alpha43(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_43_broker_layer_package_d"
    scope: str = "broker_monitoring_health"
    broker_health_monitor: bool = True
    dry_connection_status: bool = True
    simulated_latency_monitor: bool = True
    broker_diagnostics: bool = True
    monitoring_safety_policy: bool = True
    real_broker_connection_enabled: bool = False
    real_account_read_enabled: bool = False
    real_order_submit_enabled: bool = False
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
