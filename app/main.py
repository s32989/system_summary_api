from fastapi import FastAPI
from api import system
from api import health
from api import counter

app = FastAPI()

app.include_router(system.router)
app.include_router(health.router)
app.include_router(counter.router)
