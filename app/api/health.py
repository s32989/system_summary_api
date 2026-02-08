from fastapi import APIRouter

import app.services.health_eval as health

router = APIRouter(prefix="/health")

@router.get("/")
async def get_system_health():
    return health.eval_system_health()
