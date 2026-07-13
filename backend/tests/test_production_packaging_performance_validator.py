from app.production_packaging_v1.performance_validator import PerformanceValidationInputV1, PerformanceValidatorV1

def test_performance_validator_passes():
    result = PerformanceValidatorV1().validate(PerformanceValidationInputV1(avg_response_ms=100, max_memory_mb=256))
    assert result.passed is True
