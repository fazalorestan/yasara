from app.v500_alpha50_release_candidate.service import InternalRCPreparationFacadeV500Alpha50

def test_no_real_execution(): assert InternalRCPreparationFacadeV500Alpha50().report()['real_execution_enabled'] is False
