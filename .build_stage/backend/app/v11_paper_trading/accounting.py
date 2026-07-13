from app.v11_paper_trading.models import PaperAccountV11, PaperPositionV11


class PaperAccountingServiceV11:
    def __init__(self):
        self.account = PaperAccountV11()

    def update_from_positions(self, positions: list[PaperPositionV11]) -> PaperAccountV11:
        realized = sum(p.realized_pnl for p in positions)
        self.account.realized_pnl = realized
        self.account.equity = self.account.cash + realized
        return self.account
