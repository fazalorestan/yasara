from pydantic import BaseModel, Field

class DependencyValidationResultV1(BaseModel):
    valid: bool
    missing: list[str] = Field(default_factory=list)

class DependencyValidatorV1:
    def validate(self, required: list[str], installed: list[str]) -> DependencyValidationResultV1:
        installed_set = {item.lower() for item in installed}
        missing = [item for item in required if item.lower() not in installed_set]
        return DependencyValidationResultV1(valid=len(missing) == 0, missing=missing)
