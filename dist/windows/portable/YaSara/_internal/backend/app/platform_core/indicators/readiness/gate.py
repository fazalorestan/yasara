from app.platform_core.indicators.readiness.models import IndicatorReadinessCheck, IndicatorReadinessReport
from app.platform_core.indicators.registry import indicator_registry
from app.platform_core.indicators.yasara_contract import yasara_indicator_contract
from app.platform_core.indicators.pine_source.archive import pine_source_archive
from app.platform_core.indicators.settings.presets import yasara_preset_registry
from app.platform_core.indicators.settings.versioning import yasara_preset_version_registry

class YaSaraIndicatorReadinessGate:
    def run(self):
        registry = indicator_registry.seed_defaults()
        contract = yasara_indicator_contract.overlay_contract()
        archive = pine_source_archive.seed_defaults()
        presets = yasara_preset_registry.seed_defaults()
        versions = yasara_preset_version_registry.versions()

        checks = [
            IndicatorReadinessCheck("indicator_registered", "yasara" in registry, "YaSara registered in indicator registry"),
            IndicatorReadinessCheck("enabled_by_default", registry.get("yasara", {}).get("enabled_by_default") is True, "YaSara enabled by default"),
            IndicatorReadinessCheck("chart_contract_ready", contract.get("indicator") == "yasara", "Chart overlay contract ready"),
            IndicatorReadinessCheck("pine_source_archived", "yasara:v1.0" in archive, "Pine source archive ready"),
            IndicatorReadinessCheck("settings_presets_ready", len(presets) >= 4, "Default/scalping/swing/conservative presets ready"),
            IndicatorReadinessCheck("preset_versioning_ready", versions.get("current") == "v1.0", "Preset versioning ready"),
            IndicatorReadinessCheck("analysis_only_safe", True, "Execution disabled by design"),
        ]
        blockers = [c.name for c in checks if not c.ready]
        score = round(sum(1 for c in checks if c.ready) / len(checks) * 100, 2)
        return IndicatorReadinessReport(
            ready=len(blockers) == 0,
            score=score,
            checks=checks,
            blockers=blockers,
        ).to_dict() | {
            "indicator": "yasara",
            "v5_ready": len(blockers) == 0,
            "execution_allowed": False,
            "mode": "analysis_only",
        }

yasara_indicator_readiness_gate = YaSaraIndicatorReadinessGate()
