from app.platform_core.force_merge_k_sqlalchemy_gate.report import force_merge_k_sqlalchemy_gate_report_service
class ForceMergeKSQLAlchemyGateReadinessGate:
    def run(self):
        r=force_merge_k_sqlalchemy_gate_report_service.report()
        return {'ready':r['ready'] and r['force_merge_k'] and r['legacy_h_test_override'] and r['sqlalchemy_bundle_gate'] and not r['auto_trading_enabled'],'checks':r}
force_merge_k_sqlalchemy_gate_readiness_gate=ForceMergeKSQLAlchemyGateReadinessGate()
