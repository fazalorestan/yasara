class PreTradeCheckService:
    def run(self):
        return {
            "ready": True,
            "checks": {
                "risk_gate_required": True,
                "human_confirmation_required": True,
                "broker_connection_blocked": True,
                "real_execution_blocked": True,
                "auto_trading_blocked": True,
            },
            "passed": True,
            "execution_allowed": False,
        }

pre_trade_check_service = PreTradeCheckService()
