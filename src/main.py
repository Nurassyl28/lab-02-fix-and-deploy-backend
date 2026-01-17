from fastapi import FastAPI
from app.routers import items, outcomes, status

app = FastAPI(title="Course Material Service")

app.include_router(status.router, tags=["status"])
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(outcomes.router, prefix="/outcomes", tags=["outcomes"])
