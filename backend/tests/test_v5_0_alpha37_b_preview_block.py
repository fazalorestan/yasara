from app.platform_core.broker_layer.order_preview import BrokerOrderPreviewService

def test_v500_alpha37_b_preview_block(): assert BrokerOrderPreviewService().preview()['execution_allowed'] is False