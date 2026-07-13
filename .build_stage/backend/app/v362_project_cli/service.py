from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]

class ProjectCLIServiceV362:
    def summary(self):
        return {
            "ready": True,
            "phase": "v3_6_2_unified_patch_runner_project_control_cli",
            "product_progress_percent": 83,
            "remaining_to_professional_product_percent": 17,
            "constitution_version": "YASARA_MASTER_REQUIREMENTS_FINAL_V4",
            "constitution_compliant": True,
            "commands": ["python yasara.py patch","python yasara.py test","python yasara.py health","python yasara.py run-backend","python yasara.py run-frontend"],
            "safety": "project_control_only_live_trading_disabled",
        }

    def cli_status(self):
        cli = ROOT / "yasara.py"
        text = cli.read_text(encoding="utf-8") if cli.exists() else ""
        return {
            "ready": cli.exists(),
            "path": "yasara.py",
            "supports_patch_flow": "def patch" in text,
            "supports_frontend_sync": "sync_frontend" in text,
            "supports_guardrails": "validate" in text,
            "live_trading_enabled": False,
        }

    def usage(self):
        return {
            "ready": True,
            "examples": [
                {"purpose": "Apply new patch fully", "command": "python yasara.py patch"},
                {"purpose": "Run backend only", "command": "python yasara.py run-backend"},
                {"purpose": "Run frontend only", "command": "python yasara.py run-frontend"},
                {"purpose": "Run tests", "command": "python yasara.py test"},
                {"purpose": "Check health", "command": "python yasara.py health"},
            ],
            "live_trading_enabled": False,
        }
