# Apply YaSara v4.0 Market Context Engine + Personal Auto-Trade Gate

Extract into:

```text
D:\yasara_clean
```

Then run:

```cmd
cd /d D:\yasara_clean
python yasara.py patch
```

Test APIs:

```text
http://127.0.0.1:8000/api/v1/v4-0/market-context/summary
http://127.0.0.1:8000/api/v1/v4-0/market-context/quick?symbol=BTCUSDT&exchange=binance
```

Auto-trade gate test is POST:

```text
/api/v1/v4-0/market-context/autotrade-gate
```

Adds 8 tests.
