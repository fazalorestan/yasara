class InternalPortableReadinessSummary:
    def summary(self):
        return {
            "ready": True,
            "portable_layout_ready": True,
            "build_script_contract_ready": True,
            "artifact_contract_ready": True,
            "smoke_contract_ready": True,
            "requires_real_binary_builder_next": True,
            "final_exe_generated": False,
        }
internal_portable_readiness_summary = InternalPortableReadinessSummary()
