from pydantic import BaseModel, Field

class OneClickExportStatusV1(BaseModel):
    ready: bool = True
    product: str = "YaSara Professional"
    version: str = "1.0.0"
    confirmed_tests: int = 312
    final_archive_name: str = "yasara_professional_v1_0_stable.zip"
    required_steps: list[str] = Field(default_factory=lambda: [
        "run_full_tests",
        "safe_cleanup",
        "create_zip",
        "verify_archive",
    ])

class OneClickExportStatusBuilderV1:
    def build(self) -> OneClickExportStatusV1:
        return OneClickExportStatusV1()
