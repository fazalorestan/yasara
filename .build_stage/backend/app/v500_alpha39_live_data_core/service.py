from app.platform_core.live_data_pipeline.data_safety import live_data_safety_policy
from app.platform_core.live_data_pipeline.ingestion_contract import live_data_ingestion_contract
from app.platform_core.live_data_pipeline.normalizer import live_data_snapshot_normalizer
from app.platform_core.live_data_pipeline.provider_adapter import live_data_provider_adapter_contract
from app.platform_core.live_data_pipeline.readiness import live_data_pipeline_core_readiness_gate
from app.platform_core.live_data_pipeline.report import live_data_pipeline_core_report
from app.platform_core.live_data_pipeline.source_registry import live_data_source_registry
from app.v500_alpha39_live_data_core.models import LiveDataCoreSummaryV500Alpha39

class LiveDataCoreFacadeV500Alpha39:
    def summary(self): return LiveDataCoreSummaryV500Alpha39()
    def sources(self): return live_data_source_registry.list_sources()
    def ingestion_contract(self): return live_data_ingestion_contract.contract()
    def adapter_contract(self): return live_data_provider_adapter_contract.adapter_contract()
    def simulated_snapshot(self): return live_data_provider_adapter_contract.simulated_snapshot()
    def normalize_snapshot(self): return live_data_snapshot_normalizer.normalize(live_data_provider_adapter_contract.simulated_snapshot())
    def safety(self): return live_data_safety_policy.policy()
    def validate_snapshot(self): return live_data_safety_policy.validate_snapshot(self.normalize_snapshot()["snapshot"])
    def report(self): return live_data_pipeline_core_report.report()
    def readiness(self): return live_data_pipeline_core_readiness_gate.run()
    def contract(self): return {"ready": True, "live_data_pipeline": "package_a_data_source_ingestion", "execution_allowed": False}

live_data_core_facade_v500_alpha39 = LiveDataCoreFacadeV500Alpha39()
