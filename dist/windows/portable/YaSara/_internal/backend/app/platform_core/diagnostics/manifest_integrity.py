from app.platform_core.diagnostics.models import DiagnosticCheck
from app.v423_plugin_catalog.loader import PluginManifestLoaderV423

class ManifestIntegrityCheck:
    def run(self):
        loader = PluginManifestLoaderV423()
        manifests = loader.load_all()
        invalid = []
        for m in manifests:
            if not m.name or not m.version:
                invalid.append(m.name or "unknown")
        return DiagnosticCheck(
            name="manifest_integrity",
            ready=len(manifests) > 0 and len(invalid) == 0,
            severity="error" if invalid or not manifests else "info",
            detail=f"{len(manifests)} manifests loaded",
            data={"manifest_count": len(manifests), "invalid": invalid, "plugins": [m.name for m in manifests]},
        )
