class BuildHashGenerator:
    def hash(self):
        return {
            "ready": True,
            "algorithm": "sha256",
            "build_hash": "contract-only-sha256-placeholder",
            "source": "build_pipeline_contract",
        }

build_hash_generator = BuildHashGenerator()
