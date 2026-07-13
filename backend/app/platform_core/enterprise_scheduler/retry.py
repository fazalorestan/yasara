from app.platform_core.enterprise_scheduler.models import RetryPolicy

class RetryPolicyRegistry:
    def __init__(self):
        self._policies: dict[str, RetryPolicy] = {}

    def set_policy(self, task: str, policy: RetryPolicy | None = None):
        self._policies[task] = policy or RetryPolicy()
        return self._policies[task]

    def get_policy(self, task: str):
        return self._policies.get(task, RetryPolicy())

    def list(self):
        return {k: v.__dict__ for k, v in self._policies.items()}

retry_policy_registry = RetryPolicyRegistry()
