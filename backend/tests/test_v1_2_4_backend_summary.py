from app.v12_portfolio_orders.service import PortfolioOrdersServiceV12
def test_portfolio_orders_summary():
    summary = PortfolioOrdersServiceV12().summary()
    assert summary["ready"] is True
    assert summary["ui_progress_percent"] == 80
    assert "order_book" in summary["capabilities"]
