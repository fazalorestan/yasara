from app.v500_alpha50_release_candidate.service import InternalRCPreparationFacadeV500Alpha50

def test_no_real_broker(): assert InternalRCPreparationFacadeV500Alpha50().report()['real_broker_connection_enabled'] is False
