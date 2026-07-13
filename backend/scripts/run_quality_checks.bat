@echo off
set PYTHONPATH=%CD%
python -m pytest
if errorlevel 1 exit /b 1
python -m pytest --cov=app --cov-report=term-missing
