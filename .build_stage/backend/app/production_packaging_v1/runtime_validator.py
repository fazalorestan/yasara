from pydantic import BaseModel

class RuntimeValidationResultV1(BaseModel):
    ok: bool
    python_ok: bool
    backend_ok: bool
    message: str

class RuntimeValidatorV1:
    def validate(self, python_version: str, backend_importable: bool) -> RuntimeValidationResultV1:
        python_ok = python_version.startswith("3.12") or python_version.startswith("3.11")
        ok = python_ok and backend_importable
        return RuntimeValidationResultV1(ok=ok, python_ok=python_ok, backend_ok=backend_importable, message="runtime_ok" if ok else "runtime_invalid")
