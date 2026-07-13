from app.platform_core.clock import utc_now_iso

class ConfigVersionRegistry:
    def __init__(self):
        self._versions = []

    def commit(self, label: str, values: dict):
        item = {
            "version": f"cfg-{len(self._versions)+1}",
            "label": label,
            "values": values,
            "created_at": utc_now_iso(),
        }
        self._versions.append(item)
        return item

    def history(self):
        return list(self._versions)

config_version_registry = ConfigVersionRegistry()
