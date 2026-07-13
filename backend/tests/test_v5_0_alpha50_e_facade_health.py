from app.v500_alpha50_release_candidate.service import InternalRCPreparationFacadeV500Alpha50

def test_facade_health(): assert InternalRCPreparationFacadeV500Alpha50().health() is not None
