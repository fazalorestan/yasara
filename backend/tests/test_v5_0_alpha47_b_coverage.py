from app.platform_core.ci_pipeline.coverage_contract import CoverageContractService

def test_coverage(): assert CoverageContractService().contract()['coverage_enabled'] is True
