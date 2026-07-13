from app.platform_core.indicators.pine_source.models import PineUpdateSafetyContract

class PineUpdateSafetyContractService:
    def contract(self):
        return PineUpdateSafetyContract(
            editable_file="frontend/src/indicators/yasara/pine/yasara-v1.pine",
            stable_runtime_files=[
                "frontend/src/indicators/yasara/yasara-script.ts",
                "backend/app/platform_core/indicators/runtime/yasara_runtime.py",
                "frontend/src/indicators/yasara/yasara-runtime-types.ts",
            ],
            rules=[
                "Archive original Pine source before modifying runtime adapter",
                "Do not enable execution from Pine source",
                "Map Pine sections to runtime contracts explicitly",
                "Keep chart renderer contract stable",
            ],
        ).__dict__

pine_update_safety_contract_service = PineUpdateSafetyContractService()
