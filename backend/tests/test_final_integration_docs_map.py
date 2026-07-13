from app.final_integration_v1.final_docs_map import FinalDocsMapBuilderV1

def test_final_docs_map():
    docs = FinalDocsMapBuilderV1().build()
    assert any(d.filename == "docs/API_REFERENCE.md" for d in docs.docs)
