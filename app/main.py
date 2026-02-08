from fastapi import FastAPI
from api import system
from api import health

app = FastAPI()

app.include_router(system.router)
app.include_router(health.router)
