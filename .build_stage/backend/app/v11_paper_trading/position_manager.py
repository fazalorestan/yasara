from time import time
from app.v11_paper_trading.models import PaperOrderV11, PaperOrderSideV11, PaperPositionSideV11, PaperPositionV11


class PaperPositionManagerV11:
    def __init__(self):
        self.positions: dict[tuple[str, str], PaperPositionV11] = {}

    def apply_fill(self, order: PaperOrderV11) -> PaperPositionV11:
        key = (order.exchange.lower(), order.symbol.upper())
        position = self.positions.get(key) or PaperPositionV11(
            exchange=order.exchange.lower(),
            symbol=order.symbol.upper(),
        )
        qty = order.quantity
        price = order.fill_price or order.requested_price or 0.0

        if order.side == PaperOrderSideV11.BUY:
            new_qty = position.quantity + qty
            if new_qty > 0:
                position.avg_price = ((position.avg_price * position.quantity) + (price * qty)) / new_qty
            position.quantity = new_qty
        else:
            close_qty = min(position.quantity, qty)
            if close_qty > 0:
                position.realized_pnl += (price - position.avg_price) * close_qty
                position.quantity -= close_qty

        if position.quantity > 0:
            position.side = PaperPositionSideV11.LONG
        else:
            position.side = PaperPositionSideV11.FLAT
            position.quantity = 0.0

        position.updated_at = time()
        self.positions[key] = position
        return position

    def list_positions(self) -> list[PaperPositionV11]:
        return list(self.positions.values())
