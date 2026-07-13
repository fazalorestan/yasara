from pydantic import BaseModel, Field
from app.final_docs_qa_v1.documentation_index import DocumentationIndexBuilderV1
from app.final_docs_qa_v1.qa_matrix import QAMatrixBuilderV1
from app.final_docs_qa_v1.regression_matrix import RegressionMatrixBuilderV1

class DocumentationQAGateV1(BaseModel):
    passed: bool
    checks: list[str] = Field(default_factory=list)

class DocumentationQAGateBuilderV1:
    def build(self) -> DocumentationQAGateV1:
        docs = DocumentationIndexBuilderV1().build()
        qa = QAMatrixBuilderV1().build()
        regression = RegressionMatrixBuilderV1().build()
        return DocumentationQAGateV1(
            passed=bool(docs.entries and qa.items and regression.areas),
            checks=["documentation_index", "qa_matrix", "regression_matrix"],
        )
