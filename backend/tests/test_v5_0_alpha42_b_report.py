from app.platform_core.execution_engine.routing_report import OrderRoutingReport

def test_v500_alpha42_b_report(): assert OrderRoutingReport().report()['ready'] is True
