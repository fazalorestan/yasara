from app.platform_core.scanner.readiness import scanner_readiness_gate
from app.platform_core.scanner.service import scanner_foundation_service
from app.v500_alpha27_scanner.models import ScannerSummaryV500Alpha27
class ScannerFacadeV500Alpha27:
    def summary(self): return ScannerSummaryV500Alpha27()
    def watchlist(self): return scanner_foundation_service.watchlist()
    def criteria(self): return scanner_foundation_service.criteria()
    def candidates(self): return scanner_foundation_service.candidates()
    def filtered(self): return scanner_foundation_service.filtered()
    def ranked(self): return scanner_foundation_service.ranked()
    def scan(self): return scanner_foundation_service.scan()
    def risk_check(self): return scanner_foundation_service.risk_check()
    def readiness(self): return scanner_readiness_gate.run()
    def contract(self): return {"ready": True, "scanner": "foundation_only", "requires_market_data": True, "requires_risk_engine": True, "execution_allowed": False}
