from datetime import datetime, timezone
from app.platform_core.project_intelligence.state_store import project_state_store

class BuildStateWriter:
    def write_build_state(self, status: str = "success"):
        base = project_state_store.base_state()
        return {
            "ready": True,
            "written": True,
            "build_status": status,
            "last_build_time": datetime.now(timezone.utc).isoformat(),
            "store": base["source"],
            "real_execution_enabled": False,
        }

build_state_writer = BuildStateWriter()
