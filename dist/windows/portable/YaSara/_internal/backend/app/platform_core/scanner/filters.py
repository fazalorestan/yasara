class ScannerFilterPipeline:
    def apply(self, candidates: list[dict], criteria: dict):
        accepted, rejected = [], []
        for item in candidates:
            reasons = []
            if float(item.get("score", 0)) < float(criteria.get("min_score", 60)):
                reasons.append("below_min_score")
            if float(item.get("risk_pct", 999)) > float(criteria.get("max_risk_pct", 2)):
                reasons.append("risk_exceeded")
            if reasons:
                rejected.append(item | {"reject_reasons": reasons})
            else:
                accepted.append(item | {"accepted": True})
        return {"ready": True, "accepted": accepted, "rejected": rejected}
scanner_filter_pipeline = ScannerFilterPipeline()
