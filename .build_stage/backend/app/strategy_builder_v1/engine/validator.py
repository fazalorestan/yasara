from app.strategy_builder_v1.domain.models import StrategyDefinition, StrategyValidationIssue, StrategyValidationResult

class StrategyValidatorV1:
    def validate(self, strategy: StrategyDefinition) -> StrategyValidationResult:
        issues: list[StrategyValidationIssue] = []
        if not strategy.name.strip():
            issues.append(StrategyValidationIssue(field="name", message="Strategy name is required."))
        if not strategy.entry.rules:
            issues.append(StrategyValidationIssue(field="entry.rules", message="At least one entry rule is required."))
        for group_name, group in [("entry", strategy.entry), ("exit", strategy.exit), ("risk_filters", strategy.risk_filters)]:
            if group is None:
                continue
            if group.min_score < 0:
                issues.append(StrategyValidationIssue(field=f"{group_name}.min_score", message="Minimum score cannot be negative."))
            for rule in group.rules:
                if rule.weight < 0:
                    issues.append(StrategyValidationIssue(field=f"{group_name}.{rule.rule_id}.weight", message="Rule weight cannot be negative."))
                if not rule.left.key:
                    issues.append(StrategyValidationIssue(field=f"{group_name}.{rule.rule_id}.left.key", message="Left operand key is required."))
                if not rule.right.key:
                    issues.append(StrategyValidationIssue(field=f"{group_name}.{rule.rule_id}.right.key", message="Right operand key is required."))
        return StrategyValidationResult(valid=len(issues) == 0, issues=issues)
