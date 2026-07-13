from app.platform_core.ci_pipeline.ci_core import ci_pipeline_core_service
from app.platform_core.ci_pipeline.ci_dashboard_provider import ci_dashboard_provider
from app.platform_core.ci_pipeline.coverage_contract import coverage_contract_service
from app.platform_core.ci_pipeline.readiness import ci_pipeline_readiness_gate
from app.platform_core.ci_pipeline.regression_runner import regression_runner_contract
from app.platform_core.ci_pipeline.report import ci_pipeline_report_service
from app.platform_core.ci_pipeline.test_report import ci_test_report_service
from app.platform_core.ci_pipeline.test_result_registry import test_result_registry
from app.platform_core.ci_pipeline.test_runner_contract import automated_test_runner_contract
from app.v500_alpha47_ci_pipeline.models import CIPipelineSummaryV500Alpha47

class CIPipelineFacadeV500Alpha47:
    def summary(self): return CIPipelineSummaryV500Alpha47()
    def core(self): return ci_pipeline_core_service.status()
    def test_runner(self): return automated_test_runner_contract.contract()
    def regression(self): return regression_runner_contract.contract()
    def coverage(self): return coverage_contract_service.contract()
    def results(self): return test_result_registry.results()
    def test_report(self): return ci_test_report_service.report()
    def dashboard(self): return ci_dashboard_provider.dashboard()
    def report(self): return ci_pipeline_report_service.report()
    def readiness(self): return ci_pipeline_readiness_gate.run()
    def contract(self): return {"ready": True, "ci_pipeline": "package_b_automated_test_pipeline", "build_id": "2026.47.B.001"}

ci_pipeline_facade_v500_alpha47 = CIPipelineFacadeV500Alpha47()
