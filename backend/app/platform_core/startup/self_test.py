from app.platform_core.startup.backend_contract import backend_launcher_contract

class StartupSelfTest:
    def run(self):
        contract = backend_launcher_contract.contract()
        checks = {
            "backend_module_defined": contract["backend_module"] == "app.main:app",
            "host_defined": contract["host"] == "127.0.0.1",
            "port_defined": contract["port"] == 8000,
            "single_source_of_truth": contract["single_source_of_truth"] is True,
            "execution_allowed": False,
        }
        ready = all(v is True for k, v in checks.items() if k != "execution_allowed")
        return {"ready": ready, "checks": checks, "contract": contract}

startup_self_test = StartupSelfTest()
