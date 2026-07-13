from app.platform_core.broker_layer.dry_broker_router import dry_broker_router_service
from app.platform_core.broker_layer.order_adapter_contract import broker_order_adapter_contract_service
from app.platform_core.broker_layer.order_mapping import broker_order_mapping_service
from app.platform_core.broker_layer.order_routing_safety import broker_order_routing_safety_policy
from app.platform_core.broker_layer.paper_order_contract import broker_paper_order_contract_service

class BrokerOrderReport:
    def report(self):
        return {"ready": True, "adapter_contract": broker_order_adapter_contract_service.contract(), "order_mapping": broker_order_mapping_service.map_order(), "dry_route": dry_broker_router_service.route(), "paper_order": broker_paper_order_contract_service.paper_order(), "dry_submit": broker_order_adapter_contract_service.dry_submit(), "safety": broker_order_routing_safety_policy.policy(), "real_broker_connection_enabled": False, "real_order_submit_enabled": False, "real_execution_enabled": False, "auto_trading_enabled": False, "execution_allowed": False}
broker_order_report = BrokerOrderReport()
BrokerOrderReportService = BrokerOrderReport
broker_order_report_service = broker_order_report
