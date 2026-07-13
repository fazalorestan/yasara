from app.platform_core.windows_artifact_registration.exe_detector import LocalExeArtifactDetector

def test_detector(): assert LocalExeArtifactDetector().detect()['expected_exe'].endswith('YaSara.exe')
