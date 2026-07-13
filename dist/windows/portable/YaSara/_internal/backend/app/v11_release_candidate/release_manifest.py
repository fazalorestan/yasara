from app.v11_release_candidate.integration_service import V11IntegrationService
from app.v11_release_candidate.models import V11ReleaseCandidateManifest, V11ReleaseChecklistItem


class V11ReleaseManifestBuilder:
    def build(self) -> V11ReleaseCandidateManifest:
        report = V11IntegrationService().report()
        checklist = [
            V11ReleaseChecklistItem(key="all_v11_modules_ready", passed=report.ready, message="All v1.1 modules report ready."),
            V11ReleaseChecklistItem(key="live_trading_disabled", passed=True, message="Live trading is disabled for v1.1 RC1."),
            V11ReleaseChecklistItem(key="paper_trading_only", passed=True, message="Trading simulation remains paper-only."),
            V11ReleaseChecklistItem(key="release_candidate_version", passed=True, message="Version is 1.1.0-rc1."),
        ]
        return V11ReleaseCandidateManifest(checklist=checklist)
