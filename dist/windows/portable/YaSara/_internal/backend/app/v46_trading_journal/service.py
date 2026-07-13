from app.v45_paper_trading.service import PaperTradingExecutionServiceV45
from app.v46_trading_journal.models import JournalEntryV46, TradingJournalSummaryV46
from app.v46_trading_journal.reviewer import TradingJournalAIReviewerV46
from app.v46_trading_journal.store import JournalStoreV46


class TradingJournalServiceV46:
    def __init__(self):
        self.store = JournalStoreV46()
        self.reviewer = TradingJournalAIReviewerV46()
        self.paper = PaperTradingExecutionServiceV45()

    def summary(self):
        return TradingJournalSummaryV46()

    def add_entry(self, entry: JournalEntryV46):
        item = self.store.add(entry)
        return {"ready": True, "entry": item, "live_trading_enabled": False}

    def entries(self):
        return {"ready": True, "items": self.store.list(), "live_trading_enabled": False}

    def stats(self):
        items = self.store.list()
        wins = [x for x in items if x.get("pnl", 0) > 0]
        losses = [x for x in items if x.get("pnl", 0) < 0]
        total_pnl = sum(x.get("pnl", 0) for x in items)
        return {
            "ready": True,
            "count": len(items),
            "wins": len(wins),
            "losses": len(losses),
            "win_rate": round(len(wins) / len(items) * 100, 4) if items else 0,
            "total_pnl": round(total_pnl, 6),
            "average_pnl": round(total_pnl / len(items), 6) if items else 0,
            "live_trading_enabled": False,
        }

    def review(self, entry_id: str):
        entry = self.store.get(entry_id)
        if not entry:
            return {"ready": False, "error": "entry_not_found", "live_trading_enabled": False}
        return self.reviewer.review(entry)

    def import_paper_orders(self):
        account = self.paper.account()["account"]
        imported = []
        existing_ids = {x.get("source_order_id") for x in self.store.list()}
        for order in account.get("orders", []):
            if order.get("id") in existing_ids:
                continue
            side = "long" if order.get("side") == "buy" else "short"
            entry = JournalEntryV46(
                id=f"journal-{order.get('id')}",
                symbol=order.get("symbol", "BTCUSDT"),
                exchange=order.get("exchange", "binance"),
                side=side,
                entry_price=order.get("price", 0),
                exit_price=order.get("price", 0),
                quantity=order.get("quantity", 0),
                pnl=0,
                pnl_percent=0,
                emotion="neutral",
                notes="Imported from paper trading order.",
                source="paper_trading_v4_5",
            ).model_dump()
            entry["source_order_id"] = order.get("id")
            saved = self.store.add(JournalEntryV46(**{k:v for k,v in entry.items() if k in JournalEntryV46.model_fields}))
            saved["source_order_id"] = order.get("id")
            imported.append(saved)
        return {"ready": True, "imported_count": len(imported), "items": imported, "live_trading_enabled": False}
