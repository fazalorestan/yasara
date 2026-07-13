from app.v11_operations.release_verifier import ReleaseVerifierV11

def test_release_verifier_required_files():
    verifier = ReleaseVerifierV11()
    required = verifier.required_files()
    assert "windows_runtime/YaSara_Start_Backend.bat" in required
    assert "release_automation/generate_checksums.ps1" in required
