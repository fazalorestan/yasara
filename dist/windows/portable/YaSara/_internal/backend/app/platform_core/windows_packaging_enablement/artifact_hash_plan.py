class WindowsPackagingArtifactHashPlan:
    def plan(self):
        return {'ready': True,'algorithm':'sha256','targets':['dist/windows/portable/YaSara/YaSara.exe','dist/windows/portable/YaSara_Portable_Internal.zip'],'hash_required':True,'hash_generated':False,'hash_after_build_only':True}
windows_packaging_artifact_hash_plan=WindowsPackagingArtifactHashPlan()
