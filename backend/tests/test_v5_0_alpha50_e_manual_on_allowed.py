from app.v500_alpha50_release_candidate.service import InternalRCPreparationFacadeV500Alpha50

def test_manual_on_allowed(): assert InternalRCPreparationFacadeV500Alpha50().manual_toggle()['user_can_enable'] is True
