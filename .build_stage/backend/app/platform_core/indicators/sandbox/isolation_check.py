class IndicatorIsolationChecker:
    forbidden_imports = [
        "execution_engine",
        "live_trading",
        "exchange_order",
        "broker_adapter",
    ]

    def check(self, metadata: dict):
        imports = metadata.get("imports", [])
        violations = [x for x in imports if x in self.forbidden_imports]
        return {
            "ready": len(violations) == 0,
            "violations": violations,
            "execution_allowed": False,
            "mode": "static_contract_check",
        }

indicator_isolation_checker = IndicatorIsolationChecker()
