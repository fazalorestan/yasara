from app.platform_core.governance.audit_log import AuditLog
from app.platform_core.governance.metrics import Metrics

def test_v422_audit_metrics():
    a=AuditLog(); a.write('x'); assert a.list()[0]['action']=='x'
    m=Metrics(); assert m.increment('x')==1
