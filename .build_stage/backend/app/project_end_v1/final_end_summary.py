from pydantic import BaseModel
from app.project_end_v1.end_marker import ProjectEndMarkerBuilderV1

class FinalEndSummaryV1(BaseModel):
    complete: bool
    product: str
    version: str
    confirmed_tests: int
    next_action: str

class FinalEndSummaryBuilderV1:
    def build(self) -> FinalEndSummaryV1:
        marker = ProjectEndMarkerBuilderV1().build()
        return FinalEndSummaryV1(
            complete=marker.status == "finished" and marker.failed_tests == 0,
            product=marker.product,
            version=marker.version,
            confirmed_tests=marker.confirmed_tests,
            next_action="create_final_zip_archive",
        )
