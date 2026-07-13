from app.v11_operations.models import CleanupRuleV11


class CleanupPolicyBuilderV11:
    def safe_rules(self) -> list[CleanupRuleV11]:
        return [
            CleanupRuleV11(pattern="__pycache__", reason="Python cache"),
            CleanupRuleV11(pattern=".pytest_cache", reason="Pytest cache"),
            CleanupRuleV11(pattern=".mypy_cache", reason="Mypy cache"),
            CleanupRuleV11(pattern=".ruff_cache", reason="Ruff cache"),
            CleanupRuleV11(pattern="*.pyc", reason="Compiled Python cache"),
            CleanupRuleV11(pattern="*.log", reason="Runtime logs"),
            CleanupRuleV11(pattern="*.tmp", reason="Temporary files"),
        ]

    def deep_rules(self) -> list[CleanupRuleV11]:
        return self.safe_rules() + [
            CleanupRuleV11(pattern="build", reason="Build output"),
            CleanupRuleV11(pattern="dist", reason="Distribution output"),
            CleanupRuleV11(pattern="APPLY_V1_1_PHASE*.md", reason="Temporary patch guides"),
            CleanupRuleV11(pattern="V1_1_PHASE*_TEST_REPORT.md", reason="Temporary test reports"),
            CleanupRuleV11(pattern="V1_1_PHASE*_SECURITY_REVIEW.md", reason="Temporary security reports"),
            CleanupRuleV11(pattern="V1_1_PHASE*_CHANGELOG.md", reason="Temporary changelogs"),
        ]
