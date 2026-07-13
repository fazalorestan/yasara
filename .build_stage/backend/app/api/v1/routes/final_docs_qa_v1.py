from fastapi import APIRouter
from app.final_docs_qa_v1.phase3_summary import FinalDocsQASummaryBuilderV1
from app.final_docs_qa_v1.documentation_index import DocumentationIndexBuilderV1
from app.final_docs_qa_v1.documentation_gate import DocumentationQAGateBuilderV1

router = APIRouter(prefix="/final-docs-qa-v1", tags=["final-docs-qa-v1"])

@router.get("/summary")
async def summary():
    return FinalDocsQASummaryBuilderV1().build()

@router.get("/documentation-index")
async def documentation_index():
    return DocumentationIndexBuilderV1().build()

@router.get("/gate")
async def gate():
    return DocumentationQAGateBuilderV1().build()
