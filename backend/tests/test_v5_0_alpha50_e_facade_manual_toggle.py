from app.v500_alpha50_release_candidate.service import InternalRCPreparationFacadeV500Alpha50

def test_facade_manual_toggle(): assert InternalRCPreparationFacadeV500Alpha50().manual_toggle() is not None
