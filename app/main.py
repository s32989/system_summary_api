

from fastapi import FastAPI
from app.api import system
from app.api import health
from app.api import metrics

app = FastAPI()

app.include_router(system.router)
app.include_router(health.router)
app.include_router(metrics.router)

