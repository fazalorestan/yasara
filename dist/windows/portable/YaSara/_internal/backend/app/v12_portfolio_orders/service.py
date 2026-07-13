class PortfolioOrdersServiceV12:
    def summary(self):
        return {
            "ready": True,
            "phase": "v1_2_4_milestone_2_portfolio_orders_depth",
            "ui_progress_percent": 80,
            "product_progress_percent": 88,
            "capabilities": ["portfolio_summary", "positions_table", "open_orders", "order_panel", "order_book", "recent_trades", "floating_notifications"],
            "safety": "paper_trading_ui_only_live_trading_disabled"
        }
