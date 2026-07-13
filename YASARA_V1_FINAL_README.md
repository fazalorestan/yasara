# YaSara Professional v1.0 Final Stable

YaSara Professional v1.0 is the stable backend release package.

## Safety defaults

- Live trading is disabled by default.
- Telemetry is disabled by default.
- Private trading paths remain dry-run unless explicitly enabled in a future safety-gated version.

## Test

```cmd
windows_runtime\YaSara_Run_Tests.bat
```

## Start Backend

```cmd
windows_runtime\YaSara_Start_Backend.bat
```

Then open:

```text
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health
```
