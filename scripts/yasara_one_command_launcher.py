from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import time
import urllib.request
import webbrowser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
FRONTEND = ROOT / "frontend"
DEFAULT_BACKEND_PORT = 8000
DEFAULT_FRONTEND_PORT = 5173


ENGINE_ENDPOINTS = [
    "/api/v1/v4-9/market-structure/summary",
    "/api/v1/v4-10/market-structure-sprint2/summary",
    "/api/v1/v4-11/smart-money-pro/summary",
    "/api/v1/v4-12/smart-money-pro-sprint2/summary",
    "/api/v1/v4-13/ict-engine/summary",
    "/api/v1/v4-14/ai-fusion/summary",
    "/api/v1/v4-15/neowave/summary",
    "/api/v1/v4-16/neowave-sprint2/summary",
    "/api/v1/v4-17/elliott/summary",
]


def is_port_open(port: int, host: str = "127.0.0.1") -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.35)
        return sock.connect_ex((host, port)) == 0


def wait_for_url(url: str, timeout: int = 45) -> bool:
    start = time.time()
    while time.time() - start < timeout:
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                if response.status < 500:
                    return True
        except Exception:
            time.sleep(1)
    return False


def fetch_json(url: str) -> dict:
    try:
        with urllib.request.urlopen(url, timeout=3) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        return {"ready": False, "error": str(exc)}


def start_backend(port: int = DEFAULT_BACKEND_PORT) -> subprocess.Popen | None:
    if is_port_open(port):
        print(f"[YaSara] Backend already running on 127.0.0.1:{port}")
        return None

    env = os.environ.copy()
    env["PYTHONPATH"] = str(BACKEND)

    cmd = [
        sys.executable,
        "-m",
        "uvicorn",
        "app.main:app",
        "--host",
        "127.0.0.1",
        "--port",
        str(port),
        "--reload",
    ]

    print(f"[YaSara] Starting backend: {BACKEND}")
    return subprocess.Popen(
        cmd,
        cwd=str(BACKEND),
        env=env,
        creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0,
    )


def start_frontend(port: int = DEFAULT_FRONTEND_PORT) -> subprocess.Popen | None:
    if is_port_open(port):
        print(f"[YaSara] Frontend already running on 127.0.0.1:{port}")
        return None

    npm_cmd = "npm.cmd" if os.name == "nt" else "npm"
    cmd = [npm_cmd, "run", "dev", "--", "--host", "127.0.0.1", "--port", str(port)]

    print(f"[YaSara] Starting frontend: {FRONTEND}")
    return subprocess.Popen(
        cmd,
        cwd=str(FRONTEND),
        creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0,
    )


def check_engines(backend_url: str) -> dict:
    result = {"ready": True, "items": []}
    for endpoint in ENGINE_ENDPOINTS:
        payload = fetch_json(backend_url + endpoint)
        item = {
            "endpoint": endpoint,
            "ready": bool(payload.get("ready", False)),
            "phase": payload.get("phase", "unknown"),
            "error": payload.get("error"),
        }
        if not item["ready"]:
            result["ready"] = False
        result["items"].append(item)
    return result


def start(open_browser: bool = True) -> dict:
    backend_url = f"http://127.0.0.1:{DEFAULT_BACKEND_PORT}"
    frontend_url = f"http://127.0.0.1:{DEFAULT_FRONTEND_PORT}"

    start_backend(DEFAULT_BACKEND_PORT)
    backend_ready = wait_for_url(backend_url + "/api/v1/health", timeout=8)
    if not backend_ready:
        backend_ready = wait_for_url(backend_url + "/docs", timeout=30)

    start_frontend(DEFAULT_FRONTEND_PORT)
    frontend_ready = wait_for_url(frontend_url, timeout=45)

    engine_status = check_engines(backend_url) if backend_ready else {"ready": False, "items": []}

    if open_browser and frontend_ready:
        print(f"[YaSara] Opening dashboard: {frontend_url}")
        webbrowser.open(frontend_url)

    summary = {
        "ready": bool(backend_ready and frontend_ready),
        "backend": {"url": backend_url, "ready": backend_ready},
        "frontend": {"url": frontend_url, "ready": frontend_ready},
        "engines": engine_status,
        "dashboard_url": frontend_url,
        "real_order_execution_enabled": False,
        "live_trading_enabled": False,
    }

    print("[YaSara] Launcher summary:")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return summary


if __name__ == "__main__":
    start(open_browser=True)
