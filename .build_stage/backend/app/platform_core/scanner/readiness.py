from app.platform_core.scanner.service import scanner_foundation_service
class ScannerReadinessGate:
    def run(self):
        watchlist = scanner_foundation_service.watchlist()
        scan = scanner_foundation_service.scan()
        risk = scanner_foundation_service.risk_check()
        ready = watchlist["ready"] and scan["ready"] and risk["ready"]
        return {"ready": ready, "checks": {"watchlist_ready": watchlist["ready"], "scan_ready": scan["ready"], "risk_link_ready": risk["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}
scanner_readiness_gate = ScannerReadinessGate()
