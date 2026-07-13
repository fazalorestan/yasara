class CoverageContractService:
    def contract(self):
        return {
            "ready": True,
            "coverage_enabled": True,
            "coverage_report_required": True,
            "minimum_coverage_policy_defined": True,
            "coverage_threshold_mode": "progressive",
            "coverage_percent": None,
        }

coverage_contract_service = CoverageContractService()
