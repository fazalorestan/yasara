class PositionSizeCalculator:
    def calculate(self, account_equity: float, risk_pct: float, entry_price: float, stop_loss_price: float):
        if account_equity <= 0:
            return {"ready": False, "quantity": 0.0, "reason": "invalid_equity"}
        if risk_pct <= 0:
            return {"ready": False, "quantity": 0.0, "reason": "invalid_risk_pct"}
        distance = abs(entry_price - stop_loss_price)
        if distance <= 0:
            return {"ready": False, "quantity": 0.0, "reason": "invalid_stop_distance"}
        risk_amount = account_equity * (risk_pct / 100.0)
        quantity = risk_amount / distance
        return {"ready": True, "risk_amount": risk_amount, "stop_distance": distance, "quantity": quantity}

position_size_calculator = PositionSizeCalculator()
