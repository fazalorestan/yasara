import hashlib
from pathlib import Path
from app.version_v1.domain.models import ReleaseComponent, ReleaseComponentStatus, ReleaseManifest, VersionInfo

class ReleaseManifestBuilderV1:
    def build(self, root_path: str | None = None) -> ReleaseManifest:
        version = VersionInfo()
        components = [
            ReleaseComponent(name="backend", version=version.version, status=ReleaseComponentStatus.READY, notes="FastAPI backend stable."),
            ReleaseComponent(name="market_data", version=version.version, status=ReleaseComponentStatus.READY, notes="Market data foundation stable."),
            ReleaseComponent(name="market_intelligence", version=version.version, status=ReleaseComponentStatus.READY, notes="Analysis engine stable."),
            ReleaseComponent(name="decision_engine", version=version.version, status=ReleaseComponentStatus.READY, notes="Decision engine stable."),
            ReleaseComponent(name="risk_engine", version=version.version, status=ReleaseComponentStatus.READY, notes="Risk engine stable."),
            ReleaseComponent(name="backtesting", version=version.version, status=ReleaseComponentStatus.READY, notes="Backtesting engine stable."),
            ReleaseComponent(name="portfolio", version=version.version, status=ReleaseComponentStatus.READY, notes="Portfolio intelligence stable."),
            ReleaseComponent(name="paper_trading", version=version.version, status=ReleaseComponentStatus.READY, notes="Paper trading stable."),
            ReleaseComponent(name="execution_gateway", version=version.version, status=ReleaseComponentStatus.READY, notes="Execution gateway stable."),
            ReleaseComponent(name="notifications", version=version.version, status=ReleaseComponentStatus.READY, notes="Notification center stable."),
            ReleaseComponent(name="secrets_vault", version=version.version, status=ReleaseComponentStatus.READY, notes="Secrets vault stable."),
            ReleaseComponent(name="account_sync", version=version.version, status=ReleaseComponentStatus.READY, notes="Account sync scaffold stable."),
            ReleaseComponent(name="strategy_builder", version=version.version, status=ReleaseComponentStatus.READY, notes="Strategy builder stable."),
            ReleaseComponent(name="dashboard", version=version.version, status=ReleaseComponentStatus.READY, notes="Desktop dashboard backend stable."),
            ReleaseComponent(name="mobile_backend", version=version.version, status=ReleaseComponentStatus.READY, notes="Mobile backend stable."),
            ReleaseComponent(name="production_ai", version=version.version, status=ReleaseComponentStatus.READY, notes="AI assistant and production hardening stable."),
            ReleaseComponent(name="live_trading", version=version.version, status=ReleaseComponentStatus.WARNING, notes="Live trading remains gated and disabled by default."),
        ]
        checksums = {}
        if root_path:
            root = Path(root_path)
            for rel in ["backend/requirements.txt", "deployment/docker/docker-compose.production.yml", "release/manifest/yasara_v1_manifest.json"]:
                path = root / rel
                if path.exists():
                    checksums[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
        return ReleaseManifest(
            version=version,
            components=components,
            checksums=checksums,
            release_notes=[
                "YaSara v1.0 stable production source package.",
                "All core backend subsystems completed through Sprint 20.",
                "Live trading is gated and disabled by default for safety.",
                "Production deployment scaffold, docs, and release verification are included.",
            ],
        )
