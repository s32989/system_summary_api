from fastapi import APIRouter

import app.services.health_eval as health
import app.services.counters as counter

router = APIRouter(prefix="/health")

@router.get("/")
async def get_system_health():
    counter.stats['health'] += 1
    return health.eval_system_health()
