from pydantic import BaseModel
class BrokerOrderSummaryV500Alpha43(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_43_broker_layer_package_c"
    scope: str = "broker_order_adapter_paper_routing"
    order_adapter_contract: bool = True
    paper_order_contract: bool = True
    dry_broker_router: bool = True
    order_mapping_contract: bool = True
    broker_routing_safety_policy: bool = True
    real_broker_connection_enabled: bool = False
    real_order_submit_enabled: bool = False
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
