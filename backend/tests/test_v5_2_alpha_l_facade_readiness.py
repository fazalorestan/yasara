from app.v52_alpha_force_merge_k_sqlalchemy_gate.service import ForceMergeKSQLAlchemyGateFacadeV52Alpha

def test_facade_readiness(): assert ForceMergeKSQLAlchemyGateFacadeV52Alpha().readiness() is not None
