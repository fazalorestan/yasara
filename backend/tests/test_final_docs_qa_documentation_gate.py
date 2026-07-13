from app.final_docs_qa_v1.documentation_gate import DocumentationQAGateBuilderV1

def test_documentation_gate():
    gate = DocumentationQAGateBuilderV1().build()
    assert gate.passed is True
