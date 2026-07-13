class BackendLauncherContract:
    def contract(self):
        return {
            "ready": True,
            "backend_module": "app.main:app",
            "host": "127.0.0.1",
            "port": 8000,
            "command": "python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload",
            "single_source_of_truth": True,
        }

backend_launcher_contract = BackendLauncherContract()
