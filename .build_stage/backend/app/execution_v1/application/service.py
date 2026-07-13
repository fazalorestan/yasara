from app.execution_v1.domain.models import ExecutionIntent
from app.execution_v1.engine.execution_gateway import ExecutionGatewayV1

class ExecutionServiceV1:
    def __init__(self):
        self.gateway = ExecutionGatewayV1()

    async def execute(self, intent: ExecutionIntent):
        return await self.gateway.execute(intent)

    async def audit_log(self):
        return self.gateway.audit.list_entries()

execution_service_v1 = ExecutionServiceV1()
