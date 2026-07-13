from app.production_packaging_v1.environment_validator import EnvironmentValidatorV1

def test_environment_validator():
    result = EnvironmentValidatorV1().validate(["DATABASE_URL"], {})
    assert result.valid is False
    assert result.missing_keys == ["DATABASE_URL"]
