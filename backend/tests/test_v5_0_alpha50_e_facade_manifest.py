from app.v500_alpha50_release_candidate.service import InternalRCPreparationFacadeV500Alpha50

def test_facade_manifest(): assert InternalRCPreparationFacadeV500Alpha50().manifest() is not None
