import os

class IntegrationTestConfigV1:
    @staticmethod
    def enabled() -> bool:
        return os.getenv("YASARA_RUN_INTEGRATION_TESTS", "").lower() in {"1", "true", "yes", "on"}

    @staticmethod
    def require_enabled() -> None:
        if not IntegrationTestConfigV1.enabled():
            raise RuntimeError(
                "Integration tests are disabled. "
                "Set YASARA_RUN_INTEGRATION_TESTS=1 to enable real network exchange tests."
            )
