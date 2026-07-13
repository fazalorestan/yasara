from app.v500_alpha50_release_candidate.service import InternalRCPreparationFacadeV500Alpha50

def test_facade_safety_disable(): assert InternalRCPreparationFacadeV500Alpha50().safety_disable('exchange')['manual_reenable_required'] is True
