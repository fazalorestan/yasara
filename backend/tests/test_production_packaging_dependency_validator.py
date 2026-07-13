from app.production_packaging_v1.dependency_validator import DependencyValidatorV1

def test_dependency_validator_missing():
    result = DependencyValidatorV1().validate(["fastapi", "uvicorn"], ["fastapi"])
    assert result.valid is False
    assert result.missing == ["uvicorn"]
