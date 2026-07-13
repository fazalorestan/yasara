from app.final_docs_qa_v1.documentation_index import DocumentationIndexBuilderV1

def test_documentation_index():
    index = DocumentationIndexBuilderV1().build()
    assert any(e.path == "README.md" for e in index.entries)
