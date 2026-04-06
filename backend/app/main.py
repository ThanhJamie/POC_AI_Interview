from fastapi import FastAPI
from redis import Redis

from app.config import settings
from app.database import check_database_connection, init_db
from app.routers.interview import router as interview_router

app = FastAPI(title="AI Interview Backend", version="0.2.0")
app.include_router(interview_router)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


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
