from app.version_v1.domain.models import VersionInfo
from app.version_v1.engine.final_verifier import FinalReleaseVerifierV1
from app.version_v1.engine.manifest import ReleaseManifestBuilderV1

class VersionServiceV1:
    def __init__(self):
        self.manifest_builder = ReleaseManifestBuilderV1()
        self.verifier = FinalReleaseVerifierV1()

    async def version(self):
        return VersionInfo()

    async def manifest(self):
        return self.manifest_builder.build()

    async def final_verify(self):
        return self.verifier.verify()

version_service_v1 = VersionServiceV1()
