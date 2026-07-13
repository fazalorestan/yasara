from app.platform_core.cryptography_runtime_dependency_fix.report import cryptography_runtime_dependency_fix_report_service
class CryptographyRuntimeDependencyFixReadinessGate:
    def run(self):
        r = cryptography_runtime_dependency_fix_report_service.report()
        return {'ready': r['ready'] and r['fixed_import'] == 'cryptography' and r['collect_submodules'] and not r['auto_trading_enabled'], 'checks': r}
cryptography_runtime_dependency_fix_readiness_gate = CryptographyRuntimeDependencyFixReadinessGate()
