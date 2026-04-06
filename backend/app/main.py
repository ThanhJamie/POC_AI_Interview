from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis import Redis

from app.config import settings
from app.database import check_database_connection, init_db
from app.routers.interview import router as interview_router

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    init_db()
    yield


app = FastAPI(title="AI Interview Backend", version="0.2.0", lifespan=lifespan)
app.include_router(interview_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "backend"}


@app.get("/health/dependencies")
def dependency_health() -> dict[str, str]:
    db_ok = check_database_connection()
    redis_client = Redis.from_url(settings.redis_url)
    redis_ok = bool(redis_client.ping())

    return {
        "database": "ok" if db_ok else "error",
        "redis": "ok" if redis_ok else "error",
    }
