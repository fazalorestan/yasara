from app.platform_core.broker_layer.order_preview import BrokerOrderPreviewService

def test_v500_alpha37_b_notional(): assert BrokerOrderPreviewService().preview({'symbol':'BTC','side':'buy','type':'limit','quantity':2,'price':10})['notional']==20
