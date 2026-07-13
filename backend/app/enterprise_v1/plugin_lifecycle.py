from enum import StrEnum
from pydantic import BaseModel

class PluginLifecycleStateV1(StrEnum):
    INSTALLED = "installed"
    ENABLED = "enabled"
    DISABLED = "disabled"
    REMOVED = "removed"

class PluginLifecycleRecordV1(BaseModel):
    plugin_id: str
    state: PluginLifecycleStateV1 = PluginLifecycleStateV1.INSTALLED

class PluginLifecycleManagerV1:
    def enable(self, record: PluginLifecycleRecordV1) -> PluginLifecycleRecordV1:
        record.state = PluginLifecycleStateV1.ENABLED
        return record

    def disable(self, record: PluginLifecycleRecordV1) -> PluginLifecycleRecordV1:
        record.state = PluginLifecycleStateV1.DISABLED
        return record
