from app.stable_release_v1.stable_validation import StableValidationBuilderV1

def test_stable_validation():
    report = StableValidationBuilderV1().build()
    assert report.stable_ready is True
