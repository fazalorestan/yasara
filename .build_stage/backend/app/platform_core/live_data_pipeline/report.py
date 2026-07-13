from app.platform_core.live_data_pipeline.data_safety import live_data_safety_policy
from app.platform_core.live_data_pipeline.ingestion_contract import live_data_ingestion_contract
from app.platform_core.live_data_pipeline.normalizer import live_data_snapshot_normalizer
from app.platform_core.live_data_pipeline.provider_adapter import live_data_provider_adapter_contract
from app.platform_core.live_data_pipeline.source_registry import live_data_source_registry

class LiveDataPipelineCoreReport:
    def report(self):
        raw = live_data_provider_adapter_contract.simulated_snapshot()
        normalized = live_data_snapshot_normalizer.normalize(raw)
        validation = live_data_safety_policy.validate_snapshot(normalized["snapshot"])
        return {
            "ready": True,
            "sources": live_data_source_registry.list_sources(),
            "ingestion_contract": live_data_ingestion_contract.contract(),
            "adapter_contract": live_data_provider_adapter_contract.adapter_contract(),
            "normalized_snapshot": normalized,
            "validation": validation,
            "safety": live_data_safety_policy.policy(),
            "real_live_connection": False,
            "execution_allowed": False,
        }

live_data_pipeline_core_report = LiveDataPipelineCoreReport()
