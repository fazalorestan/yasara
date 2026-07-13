from pathlib import Path

ROOT = Path("..").resolve()
yasara = ROOT / "yasara.py"
if not yasara.exists():
    raise SystemExit("yasara.py not found")

src = yasara.read_text(encoding="utf-8")

start = src.find("def patch() -> None:")
if start == -1:
    raise SystemExit("patch() function not found")

next_def = src.find("\ndef test() -> None:", start)
if next_def == -1:
    raise SystemExit("test() function boundary not found")

new_patch_lines = [
"def patch() -> None:",
"    # SIMPLE_PATCH_RUNNER_FIX_V33_1",
"    scripts = [",
'        "apply_v4_18_launcher_router_patch.py",',
'        "sync_operational_frontend_status.py",',
'        "apply_v4_17_elliott_router_patch.py",',
'        "apply_v4_16_neowave_sprint2_router_patch.py",',
'        "apply_v4_15_neowave_router_patch.py",',
'        "apply_v4_14_ai_fusion_router_patch.py",',
'        "apply_v4_13_ict_engine_router_patch.py",',
'        "apply_v4_12_smart_money_pro_sprint2_router_patch.py",',
'        "apply_v4_11_smart_money_pro_router_patch.py",',
'        "apply_v4_10_market_structure_sprint2_router_patch.py",',
'        "apply_v4_9_market_structure_router_patch.py",',
'        "apply_v4_8_production_readiness_router_patch.py",',
'        "apply_v4_7_notification_alerts_router_patch.py",',
'        "apply_v4_6_trading_journal_router_patch.py",',
'        "apply_v4_5_paper_trading_router_patch.py",',
'        "apply_v4_4_backtest_benchmark_router_patch.py",',
'        "apply_v4_3_risk_engine_router_patch.py",',
'        "apply_v4_2_signal_engine_router_patch.py",',
'        "apply_v4_1_indicator_engine_router_patch.py",',
'        "apply_v4_0_market_context_router_patch.py",',
'        "apply_v3_6_1_phase_a_guardrails_router_patch.py",',
"    ]",
"",
'    for folder in [BACKEND / "scripts", ROOT / "scripts"]:',
"        if folder.exists():",
'            for item in folder.glob("apply_v*.py"):',
"                if item.is_file():",
"                    name = item.name",
"                    lowered = name.lower()",
'                    blocked = any(x in lowered for x in ["delete", "wipe", "drop", "remove_all", "format"])',
'                    if name.startswith("apply_v") and name.endswith(".py") and not blocked and name not in scripts:',
"                        scripts.append(name)",
"",
"    scripts = list(dict.fromkeys(scripts))",
"",
"    for name in scripts:",
"        path = BACKEND / \"scripts\" / name",
"        root_path = ROOT / \"scripts\" / name",
"        if path.exists():",
"            code = run([sys.executable, str(path)], cwd=BACKEND)",
"            if code != 0:",
"                raise SystemExit(code)",
"        elif root_path.exists():",
"            code = run([sys.executable, str(root_path)], cwd=ROOT)",
"            if code != 0:",
"                raise SystemExit(code)",
"",
'    print("\\n[YaSara] Patch flow completed successfully.")',
"",
"",
]
new_patch = "\n".join(new_patch_lines)

src = src[:start] + new_patch + src[next_def + 1:]
yasara.write_text(src, encoding="utf-8")

router_file = Path("app/api/v1/router.py")
text = router_file.read_text(encoding="utf-8")
module_name = "v500_alpha33_1_simple_patch_runner_v1"
if module_name not in text:
    marker = "from app.api.v1.routes import "
    if marker in text:
        text = text.replace(marker, marker + module_name + ", ", 1)
    else:
        text = f"from app.api.v1.routes import {module_name}\n" + text
    text += f"\napi_router.include_router({module_name}.router)\n"
router_file.write_text(text, encoding="utf-8")

print("YaSara v5.0-alpha.33.1 Simple Patch Runner fix applied.")
