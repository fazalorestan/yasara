class LiveDataSnapshotNormalizer:
    def normalize(self, snapshot: dict):
        return {
            "ready": True,
            "snapshot": {
                "source_id": snapshot.get("source_id", "unknown"),
                "symbol": str(snapshot.get("symbol", "")).replace("/", "").upper(),
                "price": float(snapshot.get("price", 0.0)),
                "timestamp": int(snapshot.get("timestamp", 0)),
                "metadata": snapshot.get("metadata", {}),
            },
            "real_connection": False,
        }

live_data_snapshot_normalizer = LiveDataSnapshotNormalizer()
