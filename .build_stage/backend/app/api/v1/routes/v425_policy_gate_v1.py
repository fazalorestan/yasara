from fastapi import APIRouter
from app.v425_policy_gate.models import PolicyContextV425, PolicyRequirementV425
from app.v425_policy_gate.service import PolicyGateServiceV425

router = APIRouter(prefix="/v4-25/policy-gate", tags=["v4.25-policy-gate"])
_service = PolicyGateServiceV425()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/evaluate")
async def evaluate(context: PolicyContextV425, requirement: PolicyRequirementV425):
    return _service.evaluate(context, requirement)

@router.get("/execution-contract")
async def execution_contract():
    return _service.execution_contract()

@router.post("/validate-analysis-payload")
async def validate_analysis_payload(payload: dict):
    return _service.validate_analysis_payload(payload)
