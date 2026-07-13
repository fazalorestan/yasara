class BrokerAccountSnapshotService:
    def balances(self):
        return {"ready": True, "balances": [{"asset": "USDT", "free": 10000.0, "locked": 0.0}, {"asset": "BTC", "free": 0.1, "locked": 0.0}], "real_connection": False}

    def positions(self):
        return {"ready": True, "positions": [{"symbol": "BTCUSDT", "size": 0.1, "entry_price": 45000.0, "unrealized_pnl": 500.0}], "real_connection": False}

    def snapshot(self):
        return {"ready": True, "balances": self.balances()["balances"], "positions": self.positions()["positions"], "real_connection": False, "execution_allowed": False}

broker_account_snapshot_service = BrokerAccountSnapshotService()
