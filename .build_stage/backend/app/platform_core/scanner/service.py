from app.platform_core.scanner.candidates import scanner_candidate_provider
from app.platform_core.scanner.filters import scanner_filter_pipeline
from app.platform_core.scanner.ranking import scanner_ranking_service
from app.platform_core.scanner.risk_link import scanner_risk_link_service
from app.platform_core.scanner.watchlist import scanner_watchlist_service

class ScannerFoundationService:
    def watchlist(self): return scanner_watchlist_service.default_watchlist()
    def criteria(self): return {"ready": True, "min_score": 60.0, "max_risk_pct": 2.0, "require_trend_alignment": True, "require_volume_confirmation": False}
    def candidates(self): return {"ready": True, "items": scanner_candidate_provider.sample_candidates()}
    def filtered(self): return scanner_filter_pipeline.apply(scanner_candidate_provider.sample_candidates(), self.criteria())
    def ranked(self): return scanner_ranking_service.rank(self.filtered()["accepted"])
    def risk_check(self): return scanner_risk_link_service.check(scanner_candidate_provider.sample_candidates()[0])
    def scan(self):
        filtered = self.filtered()
        ranked = scanner_ranking_service.rank(filtered["accepted"])
        return {"ready": True, "total": len(scanner_candidate_provider.sample_candidates()), "accepted": len(filtered["accepted"]), "rejected": len(filtered["rejected"]), "ranked": ranked["items"], "execution_allowed": False}
scanner_foundation_service = ScannerFoundationService()
