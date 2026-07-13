from pydantic import BaseModel

class FrontendCompatibilitySummaryV4211(BaseModel):
    ready: bool = True
    phase: str = "v4_21_1_frontend_backward_compatibility_layer"
    scope: str = "frontend_test_compatibility"
    preserves_v420_ui: bool = True
    compatibility_tokens: list[str] = ["WorkspaceButton", "AI Signals"]
    safety: str = "ui_compatibility_only_no_real_execution"
    constitution_compliant: bool = True
