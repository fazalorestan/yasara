from pydantic import BaseModel, Field

class ExportRequestV1(BaseModel):
    format: str = "json"
    sections: list[str] = Field(default_factory=list)

class ExportPlanV1(BaseModel):
    filename: str
    mime_type: str
    sections: list[str]

class ExportPlannerV1:
    def plan(self, request: ExportRequestV1) -> ExportPlanV1:
        mime = "application/json" if request.format == "json" else "text/csv"
        return ExportPlanV1(filename=f"yasara_export.{request.format}", mime_type=mime, sections=request.sections)
