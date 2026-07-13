class PluginDependencyValidatorV424:
    def validate(self, manifests):
        names = {m.name for m in manifests}
        issues = []
        for manifest in manifests:
            for dep in manifest.dependencies:
                if dep not in names:
                    issues.append({
                        "plugin": manifest.name,
                        "missing_dependency": dep,
                        "severity": "warning",
                    })
        return {
            "ready": len(issues) == 0,
            "issue_count": len(issues),
            "issues": issues,
        }
