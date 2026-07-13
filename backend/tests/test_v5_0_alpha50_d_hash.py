from app.platform_core.windows_artifact_registration.hash_generator import LocalExeHashGeneratorContract

def test_hash(): assert LocalExeHashGeneratorContract().contract()['algorithm']=='sha256'
