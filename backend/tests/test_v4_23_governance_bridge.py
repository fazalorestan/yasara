from app.v423_plugin_catalog.governance_bridge import GovernanceContextV423, PluginGovernanceBridgeV423
from app.v423_plugin_catalog.models import PluginManifestV423

def test_v423_governance_bridge():
    manifest = PluginManifestV423(name="x", version="1", required_permissions=["a"], required_licenses=["pro"], feature_flags=["f"])
    context = GovernanceContextV423(permissions=["a"], licenses=["pro"], feature_flags={"f": True})
    result = PluginGovernanceBridgeV423().evaluate(manifest, context)
    assert result["allowed"] is True
