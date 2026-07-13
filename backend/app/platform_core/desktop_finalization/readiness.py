from app.platform_core.desktop_finalization.report import internal_desktop_build_finalization_report_service

class InternalDesktopBuildFinalizationReadinessGate:
    def run(self):
        r = internal_desktop_build_finalization_report_service.report()
        ready = (
            r["ready"]
            and r["final_report"]["desktop_host_ready"]
            and r["portable_readiness"]["ready"]
            and r["smoke_finalization"]["smoke_finalized"]
            and r["sprint_completion"]["sprint_complete"]
            and r["exe_handoff"]["ready"]
            and r["final_exe_generated"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "desktop_host_ready": r["final_report"]["desktop_host_ready"],
                "portable_ready": r["portable_readiness"]["ready"],
                "smoke_finalized": r["smoke_finalization"]["smoke_finalized"],
                "sprint_complete": r["sprint_completion"]["sprint_complete"],
                "exe_handoff_ready": r["exe_handoff"]["ready"],
                "final_exe_generated": r["final_exe_generated"],
            },
        }
internal_desktop_build_finalization_readiness_gate = InternalDesktopBuildFinalizationReadinessGate()
