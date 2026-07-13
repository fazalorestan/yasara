# YaSara v1.0 Stable Release Guide

## Required verification
1. Extract source package.
2. Install backend dependencies.
3. Run all tests.
4. Start backend.
5. Check `/health`.
6. Check `/docs`.
7. Check `/api/v1/version-v1/final-verify`.

## Production reminders
- Replace `.env.production.example` secrets.
- Use PostgreSQL in production.
- Configure HTTPS through Nginx.
- Keep live trading disabled until explicitly approved.
- Store backups outside the application directory.
