from fastapi import FastAPI
from app.routers import items, status

app = FastAPI(title="Course Material Service")

app.include_router(status.router, tags=["status"])
app.include_router(items.router, prefix="/items", tags=["items"])
