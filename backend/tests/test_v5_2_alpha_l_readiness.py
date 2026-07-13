from app.platform_core.force_merge_k_sqlalchemy_gate.readiness import ForceMergeKSQLAlchemyGateReadinessGate

def test_readiness(): assert ForceMergeKSQLAlchemyGateReadinessGate().run()['ready'] is True
