from app.platform_core.release.compatibility_matrix import CompatibilityMatrix
from app.platform_core.release.plugin_readiness import PluginReadinessMatrix
from app.platform_core.release.readiness_gate import release_readiness_gate
from app.platform_core.release.security_readiness import SecurityReadinessReport
from app.v431_release_readiness.models import ReleaseReadinessSummaryV431

class ReleaseReadinessServiceV431:
    def summary(self):
        return ReleaseReadinessSummaryV431()

    def gate(self):
        return release_readiness_gate.run()

    def compatibility(self):
        return CompatibilityMatrix().matrix()

    def plugins(self):
        return PluginReadinessMatrix().matrix()

    def security(self):
        return SecurityReadinessReport().report()
