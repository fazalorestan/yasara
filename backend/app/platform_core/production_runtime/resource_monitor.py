class RuntimeResourceMonitor:
    def snapshot(self):
        return {"ready": True, "cpu_percent": 0.0, "memory_percent": 0.0, "disk_percent": 0.0, "source": "contract_only", "within_limits": True, "real_execution_enabled": False}
runtime_resource_monitor = RuntimeResourceMonitor()
