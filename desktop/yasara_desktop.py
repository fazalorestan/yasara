from pathlib import Path
import faulthandler, json, os, sys, threading, time, traceback, urllib.request, webbrowser

BUILD_ID = "2026.52.N.001"
HOST = "127.0.0.1"
PORT = 8000
HEALTH_CANDIDATES = [
    f"http://{HOST}:{PORT}/api/v1/health",
    f"http://{HOST}:{PORT}/health",
    f"http://{HOST}:{PORT}/docs",
    f"http://{HOST}:{PORT}/openapi.json",
]

def project_root():
    return Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parents[1]

def source_root(root):
    internal = root / "_internal"
    return internal if getattr(sys, "frozen", False) and internal.exists() else root

def append_log(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", errors="replace") as f:
        f.write(text.rstrip() + "\n")

def probe(url):
    try:
        with urllib.request.urlopen(url, timeout=2) as r:
            return 200 <= r.status < 500, r.status
    except Exception as exc:
        return False, str(exc)

def wait_health(seconds=60):
    deadline = time.time() + seconds
    last = {}
    while time.time() < deadline:
        for url in HEALTH_CANDIDATES:
            ok, status = probe(url)
            last[url] = status
            if ok:
                return True, url, status, last
        time.sleep(0.5)
    return False, None, None, last

def backend_thread_main(root, stdout_path, stderr_path):
    try:
        src = source_root(root)
        backend_dir = src / "backend"
        if str(backend_dir) not in sys.path:
            sys.path.insert(0, str(backend_dir))
        os.chdir(str(backend_dir))
        append_log(stdout_path, f"[{BUILD_ID}] backend cwd={backend_dir}")
        append_log(stdout_path, f"[{BUILD_ID}] importing app.main")
        import uvicorn
        import app.main as app_main
        asgi_app = getattr(app_main, "app", None)
        append_log(stdout_path, f"[{BUILD_ID}] app import complete app_present={asgi_app is not None}")
        uvicorn.run(asgi_app or "app.main:app", host=HOST, port=PORT, log_level="info", access_log=False)
    except Exception:
        append_log(stderr_path, traceback.format_exc())

def dump_thread_diagnostics(stderr_path):
    try:
        with stderr_path.open("a", encoding="utf-8", errors="replace") as f:
            f.write("\n--- YaSara backend hang diagnostics ---\n")
            f.write(f"build_id={BUILD_ID}\n")
            f.write(f"cwd={os.getcwd()}\n")
            f.write(f"threads={[t.name for t in threading.enumerate()]}\n")
            faulthandler.dump_traceback(file=f, all_threads=True)
            f.write("\n--- end diagnostics ---\n")
    except Exception:
        pass

def start_backend(root):
    backend_dir = source_root(root) / "backend"
    reports = root / "runtime_reports"
    reports.mkdir(parents=True, exist_ok=True)
    stdout_path = reports / "backend_stdout.log"
    stderr_path = reports / "backend_stderr.log"
    stdout_path.write_text("", encoding="utf-8")
    stderr_path.write_text("", encoding="utf-8")
    if not (backend_dir / "app").exists():
        stderr_path.write_text("backend_app_missing", encoding="utf-8")
        return None, "backend_app_missing", stdout_path, stderr_path
    t = threading.Thread(target=backend_thread_main, args=(root, stdout_path, stderr_path), daemon=False, name="YaSaraEmbeddedBackend")
    t.start()
    return t, "thread_started", stdout_path, stderr_path

def main():
    root = project_root()
    backend_thread, backend_status, stdout_path, stderr_path = start_backend(root)
    health_ok, health_url, health_status, probe_results = wait_health(60) if backend_thread else (False, None, None, {})
    if backend_thread and not health_ok:
        dump_thread_diagnostics(stderr_path)
    out = root / "runtime_reports" / "launcher_report.json"
    out.write_text(json.dumps({
        "app":"YaSara","launcher":"native_windows_launcher","backend_runner":"in_process_thread","build_id":BUILD_ID,
        "started":True,"backend_status":backend_status,"backend_thread_alive":bool(getattr(backend_thread,"is_alive",lambda:False)()),
        "backend_health_ok":health_ok,"backend_health_url":health_url,"backend_health_status":health_status,
        "health_candidates":HEALTH_CANDIDATES,"probe_results":probe_results,
        "backend_stdout_log":str(stdout_path),"backend_stderr_log":str(stderr_path),
        "diagnostics_enabled":True,"signal_only_default":True,"auto_trading_enabled":False,
        "cwd":os.getcwd(),"root":str(root),"timestamp":time.time()
    }, indent=2), encoding="utf-8")
    src = source_root(root)
    dashboard = src / "frontend" / "dist" / "index.html"
    if dashboard.exists() and health_ok:
        webbrowser.open(f"http://{HOST}:{PORT}/")
    else:
        print("Dashboard not found:", dashboard)
    print("YaSara Native Launcher started")
    print("Backend Runner: in_process_thread")
    print("Backend Status:", backend_status)
    print("Backend Health:", "OK" if health_ok else "NOT READY")
    print("Backend Health URL:", health_url)
    print("Runtime report:", out)
    print("Signal Only Mode: ON")
    print("Auto Trading: OFF")
    if backend_thread:
        try:
            backend_thread.join()
        except KeyboardInterrupt:
            pass
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
