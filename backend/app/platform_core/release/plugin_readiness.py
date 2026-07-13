from app.v423_plugin_catalog.loader import PluginManifestLoaderV423

class PluginReadinessMatrix:
    def matrix(self):
        manifests = PluginManifestLoaderV423().load_all()
        rows = []
        for m in manifests:
            rows.append({
                "plugin": m.name,
                "version": m.version,
                "manifest": True,
                "routes_declared": len(m.routes) > 0,
                "feature_flags_declared": isinstance(m.feature_flags, list),
                "permissions_declared": isinstance(m.required_permissions, list),
                "licenses_declared": isinstance(m.required_licenses, list),
                "ready": True,
            })
        return {
            "ready": len(rows) > 0,
            "plugin_count": len(rows),
            "plugins": rows,
        }
