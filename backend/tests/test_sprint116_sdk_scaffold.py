from app.release_pro_v1.sdk_scaffold import SDKScaffoldBuilderV1

def test_sdk_scaffold_python():
    sdk = SDKScaffoldBuilderV1().python_sdk()
    assert sdk.language == "python"
    assert any(e.name == "health" for e in sdk.endpoints)
