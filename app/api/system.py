from fastapi import APIRouter
from typing import Literal

import app.services.system_info as sys_info

router = APIRouter(prefix="/system")

@router.get("/info")
async def get_system_info():
    return sys_info.system_health_check()

@router.get("/top")
async def get_system_processes(by: Literal["cpu", "mem"] = 'cpu', limit: int = 10):
    return sys_info.get_system_processes(by, limit)