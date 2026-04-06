from fastapi import FastAPI

app = FastAPI(title="AI Interview Worker", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "ai-worker"}


@app.get("/gpu-check")
def gpu_check() -> dict[str, str]:
    return {
        "status": "ok",
        "message": "Run `nvidia-smi` inside container to verify GPU visibility.",
    }
