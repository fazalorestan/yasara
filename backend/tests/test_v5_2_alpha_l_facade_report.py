from app.v52_alpha_force_merge_k_sqlalchemy_gate.service import ForceMergeKSQLAlchemyGateFacadeV52Alpha

def test_facade_report(): assert ForceMergeKSQLAlchemyGateFacadeV52Alpha().report() is not None
