class LocalExeArtifactDetector:
    def detect(self):
        return {'ready': True,'build_id':'2026.50.D.001','expected_exe':'dist/windows/portable/YaSara/YaSara.exe','exists':False,'detection_mode':'post_build','final_exe_generated':False}
local_exe_artifact_detector=LocalExeArtifactDetector()
