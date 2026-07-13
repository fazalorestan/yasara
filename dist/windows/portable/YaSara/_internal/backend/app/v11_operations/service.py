from app.v11_operations.cleanup_policy import CleanupPolicyBuilderV11
from app.v11_operations.health_check import ProjectHealthCheckerV11
from app.v11_operations.project_info import ProjectInfoBuilderV11
from app.v11_operations.release_verifier import ReleaseVerifierV11


class OperationsMaintenanceServiceV11:
    def cleanup_policy(self, deep: bool = False):
        builder = CleanupPolicyBuilderV11()
        return builder.deep_rules() if deep else builder.safe_rules()

    def health(self):
        return ProjectHealthCheckerV11().check()

    def info(self):
        return ProjectInfoBuilderV11().build()

    def release(self):
        return ReleaseVerifierV11().verify()

    def summary(self) -> dict:
        health = self.health()
        release = self.release()
        return {
            "ready": health.ready and release.ready,
            "health_ready": health.ready,
            "release_ready": release.ready,
            "version": self.info().version,
            "cleanup_rules": len(self.cleanup_policy()),
        }
