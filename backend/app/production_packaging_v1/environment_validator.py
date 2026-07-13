from pydantic import BaseModel, Field

class EnvironmentValidationResultV1(BaseModel):
    valid: bool
    missing_keys: list[str] = Field(default_factory=list)

class EnvironmentValidatorV1:
    def validate(self, required_keys: list[str], env: dict[str, str]) -> EnvironmentValidationResultV1:
        missing = [key for key in required_keys if not env.get(key)]
        return EnvironmentValidationResultV1(valid=len(missing) == 0, missing_keys=missing)
