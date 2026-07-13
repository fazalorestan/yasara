from app.v500_alpha50_release_candidate.service import InternalRCPreparationFacadeV500Alpha50

def test_signal_only_default(): assert InternalRCPreparationFacadeV500Alpha50().summary().signal_only_default is True
