from app.v21_real_data.service import RealDataActivationServiceV21

def test_real_data_summary():
    summary = RealDataActivationServiceV21().summary()
    assert summary.operational_progress_percent == 60
    assert summary.remaining_to_full_operational_percent == 40
