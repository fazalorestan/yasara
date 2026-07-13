from app.enterprise_v1.startup_validation import StartupValidatorV1

def test_startup_validation():
    report = StartupValidatorV1().validate()
    assert report.valid is True
