# Apply YaSara v2.5 Risk, Backtest & Paper Trading Activation

Extract into `D:\yasara_clean`.

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v2_5_risk_backtest_paper_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Test:
`http://127.0.0.1:8000/api/v1/v2-5/risk-backtest-paper/summary`

Operational progress: 98%
Remaining: 2%

Adds 6 tests.
