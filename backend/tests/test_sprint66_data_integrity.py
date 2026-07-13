from app.connectivity_v1.data_integrity import DataIntegrityCheckerV1

def test_data_integrity_finds_gap():
    result = DataIntegrityCheckerV1().find_time_gaps([0, 60, 180], expected_interval=60)
    assert result.gaps == [(60, 180)]
