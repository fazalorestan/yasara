from app.account_sync_v1.domain.models import AccountSyncSnapshot, OrderRecoveryReport

class OrderRecoveryEngineV1:
    def recover(self, snapshot: AccountSyncSnapshot, local_orders: list[dict] | None = None) -> OrderRecoveryReport:
        local_orders = local_orders or []
        exchange_order_ids = {str(o.get("exchange_order_id") or o.get("orderId")) for o in snapshot.open_orders}
        recovered = []
        missing = []
        warnings = []

        for order in local_orders:
            oid = str(order.get("exchange_order_id") or order.get("orderId"))
            if oid in exchange_order_ids:
                recovered.append(order)
            else:
                missing.append(order)

        if missing:
            warnings.append("Some local orders were not found in exchange open order snapshot.")

        return OrderRecoveryReport(
            owner_id=snapshot.owner_id,
            exchange=snapshot.exchange,
            recovered_orders=recovered,
            missing_orders=missing,
            warnings=warnings,
        )
