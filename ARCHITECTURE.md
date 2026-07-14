# Architecture

`tool_discovery.py` resolves Python, Git, Node, and NPM without shell execution and supports Windows `.cmd` tools.

`service.py` owns the release state machine:

1. Tool validation
2. Git repository, branch, and remote validation
3. Stage changes
4. Whitespace/conflict validation
5. Existing YaSara test command
6. Frontend Vite build
7. Windows EXE build
8. Optional packaged backend verification
9. EXE validation
10. Dashboard stability validation
11. Re-stage generated reports/artifacts
12. Commit only after every validation succeeds
13. Push only after commit succeeds

Every command writes an isolated log and updates an atomic JSON report. The Dashboard layout and `yasara.py` remain untouched.
