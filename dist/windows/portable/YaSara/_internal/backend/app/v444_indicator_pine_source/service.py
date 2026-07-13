from app.platform_core.indicators.pine_source.archive import pine_source_archive
from app.platform_core.indicators.pine_source.mapping import pine_to_runtime_mapping_registry
from app.platform_core.indicators.pine_source.update_contract import pine_update_safety_contract_service
from app.v444_indicator_pine_source.models import IndicatorPineSourceSummaryV444

class IndicatorPineSourceServiceV444:
    def summary(self):
        return IndicatorPineSourceSummaryV444()

    def archive(self):
        return {"ready": True, "archive": pine_source_archive.seed_defaults()}

    def mapping(self):
        return {"ready": True, "mapping": pine_to_runtime_mapping_registry.seed_defaults()}

    def update_contract(self):
        return {"ready": True, "contract": pine_update_safety_contract_service.contract()}

    def source_status(self):
        return {
            "ready": True,
            "indicator": "yasara",
            "source_archived": True,
            "runtime_mapped": True,
            "execution_allowed": False,
            "mode": "source_archive_only",
        }
