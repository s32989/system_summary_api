from fastapi import FastAPI
from api import system
from api import health
from api import metrics

app = FastAPI()

app.include_router(system.router)
app.include_router(health.router)
app.include_router(metrics.router)
