from app.platform_core.build_pipeline.hash_generator import BuildHashGenerator

def test_hash(): assert BuildHashGenerator().hash()['algorithm']=='sha256'
