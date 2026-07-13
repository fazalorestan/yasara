class LocalExeHashGeneratorContract:
    def contract(self):
        return {'ready': True,'algorithm':'sha256','target':'dist/windows/portable/YaSara/YaSara.exe','output':'dist/windows/artifacts/YaSara.exe.sha256','requires_existing_artifact':True,'hash_generated':False}
local_exe_hash_generator_contract=LocalExeHashGeneratorContract()
