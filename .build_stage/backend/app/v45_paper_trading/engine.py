class PaperExecutionSimulatorV45:
    def mark_price(self, quote):
        return float(quote.get("last") or quote.get("price") or 0)

    def place_order(self, account, order, fill_price):
        if order.quantity <= 0:
            return account, {"accepted": False, "reason": "invalid_quantity"}

        side_sign = 1 if order.side == "buy" else -1
        notional = order.quantity * fill_price
        order_id = f"paper-{len(account['orders']) + 1}"

        order_item = {
            "id": order_id,
            "symbol": order.symbol.upper(),
            "exchange": order.exchange,
            "side": order.side,
            "order_type": order.order_type,
            "quantity": order.quantity,
            "price": fill_price,
            "notional": round(notional, 6),
            "status": "filled",
            "source": order.source,
            "real_order_execution_enabled": False,
        }

        account["orders"].append(order_item)

        position = self._find_position(account, order.symbol, order.exchange)
        if position is None:
            account["positions"].append({
                "symbol": order.symbol.upper(),
                "exchange": order.exchange,
                "side": "long" if side_sign > 0 else "short",
                "quantity": order.quantity,
                "avg_entry": fill_price,
                "mark_price": fill_price,
                "unrealized_pnl": 0.0,
            })
        else:
            self._update_position(account, position, order, fill_price, side_sign)

        return account, {"accepted": True, "order": order_item}

    def _find_position(self, account, symbol, exchange):
        for p in account["positions"]:
            if p["symbol"] == symbol.upper() and p["exchange"] == exchange:
                return p
        return None

    def _update_position(self, account, position, order, fill_price, side_sign):
        current_sign = 1 if position["side"] == "long" else -1
        if current_sign == side_sign:
            total_qty = position["quantity"] + order.quantity
            if total_qty > 0:
                position["avg_entry"] = ((position["avg_entry"] * position["quantity"]) + (fill_price * order.quantity)) / total_qty
            position["quantity"] = total_qty
        else:
            closing_qty = min(position["quantity"], order.quantity)
            pnl = (fill_price - position["avg_entry"]) * closing_qty * current_sign
            account["realized_pnl"] += pnl
            account["balance"] += pnl
            position["quantity"] -= closing_qty
            if position["quantity"] <= 0:
                account["positions"].remove(position)
                remaining = order.quantity - closing_qty
                if remaining > 0:
                    account["positions"].append({
                        "symbol": order.symbol.upper(),
                        "exchange": order.exchange,
                        "side": "long" if side_sign > 0 else "short",
                        "quantity": remaining,
                        "avg_entry": fill_price,
                        "mark_price": fill_price,
                        "unrealized_pnl": 0.0,
                    })

    def mark_to_market(self, account, prices):
        unrealized = 0
        for p in account["positions"]:
            key = f"{p['exchange']}:{p['symbol']}"
            price = prices.get(key, p["mark_price"])
            p["mark_price"] = price
            sign = 1 if p["side"] == "long" else -1
            p["unrealized_pnl"] = round((price - p["avg_entry"]) * p["quantity"] * sign, 6)
            unrealized += p["unrealized_pnl"]
        account["unrealized_pnl"] = round(unrealized, 6)
        account["equity"] = round(account["balance"] + unrealized, 6)
        return account
