from fastapi import APIRouter

import app.services.counters as counter

router = APIRouter(prefix="/metrics")

@router.get("/run_time")
async def get_run_time():
    counter.stats['metrics/run_time'] += 1
    return counter.get_runtime()

@router.get("/call_count")
async def get_call_count():
    counter.stats['metrics/call_count'] += 1
    return counter.get_call_count()

