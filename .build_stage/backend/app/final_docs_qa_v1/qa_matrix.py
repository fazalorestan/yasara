from pydantic import BaseModel, Field

class QAMatrixItemV1(BaseModel):
    area: str
    test_command: str
    required: bool = True

class QAMatrixV1(BaseModel):
    items: list[QAMatrixItemV1] = Field(default_factory=list)

class QAMatrixBuilderV1:
    def build(self) -> QAMatrixV1:
        return QAMatrixV1(items=[
            QAMatrixItemV1(area="full_regression", test_command="python -m pytest tests"),
            QAMatrixItemV1(area="health", test_command="curl http://127.0.0.1:8000/health"),
            QAMatrixItemV1(area="release_summary", test_command="curl http://127.0.0.1:8000/api/v1/stable-release-v1/summary"),
            QAMatrixItemV1(area="docs", test_command="manual review"),
        ])
