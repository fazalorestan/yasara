from pydantic import BaseModel
from app.final_export_scripts_v1.export_status import OneClickExportStatusBuilderV1

class OneClickExportSummaryV1(BaseModel):
    ready: bool
    archive_name: str
    message: str

class OneClickExportSummaryBuilderV1:
    def build(self) -> OneClickExportSummaryV1:
        status = OneClickExportStatusBuilderV1().build()
        return OneClickExportSummaryV1(
            ready=status.ready,
            archive_name=status.final_archive_name,
            message="Final export script is ready. Run backend/scripts/one_click_final_export.bat from the project.",
        )
