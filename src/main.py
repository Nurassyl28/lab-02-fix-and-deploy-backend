"""Course Material Service - FastAPI application.

A read-only service that serves course-related items (labs, tasks, steps)
from JSON data files.
"""

from fastapi import FastAPI
from app.routers import items, status, outcomes

app = FastAPI(
    title="Course Material Service",
    description="A read-only API for accessing course structure and learning materials.",
    version="0.1.0",
)

app.include_router(status.router, tags=["status"])
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(outcomes.router, prefix="/outcomes", tags=["outcomes"])
