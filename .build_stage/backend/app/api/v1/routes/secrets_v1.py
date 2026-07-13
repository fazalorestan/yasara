from fastapi import APIRouter, HTTPException
from app.secrets_v1.application.service import secrets_vault_service_v1
from app.secrets_v1.domain.models import SecretCreateRequest

router = APIRouter(prefix="/secrets-v1", tags=["secrets-v1"])

@router.post("")
async def create_secret(payload: SecretCreateRequest):
    return await secrets_vault_service_v1.create_secret(payload)

@router.get("")
async def list_secrets(owner_id: str = "default"):
    return await secrets_vault_service_v1.list_secrets(owner_id)

@router.delete("/{secret_id}")
async def disable_secret(secret_id: str):
    result = await secrets_vault_service_v1.disable_secret(secret_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Secret not found")
    return result
