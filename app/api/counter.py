from fastapi import APIRouter

import app.services.counters as counter

router = APIRouter(prefix="/counter")

@router.get("/")
async def get_call_count():
    counter.stats['counter'] += 1
    return counter.get_call_count()
