from dataclasses import dataclass, field
from typing import Any

@dataclass
class StandardAPIResponse:
    ready: bool = True
    version: str = "v4.26"
    module: str = "platform"
    status: str = "ok"
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)

    def to_dict(self):
        return {
            "ready": self.ready,
            "version": self.version,
            "module": self.module,
            "status": self.status,
            "data": self.data,
            "errors": self.errors,
            "warnings": self.warnings,
            "meta": self.meta,
        }

class BaseContract:
    contract_name = "base"
    contract_version = "v4.26"

    def describe(self):
        return {
            "contract_name": self.contract_name,
            "contract_version": self.contract_version,
        }
