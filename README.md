# AI Voice Interviewer PoC - Phase 0

Phase 0 provides a reproducible local infrastructure baseline with Docker Compose,
GPU-ready AI worker, PostgreSQL bootstrap extensions, and VS Code dev container support.

## Services

- frontend (Next.js)
- backend (FastAPI)
- ai-worker (CUDA-ready FastAPI worker)
- db (PostgreSQL with pgvector)
- redis

## Quick Start

1. Copy environment template:

```bash
cp .env.example .env
```

2. Build and start services:

```bash
docker compose up --build -d
```

3. Check core health endpoints:

```bash
curl http://localhost:8000/health
curl http://localhost:8001/health
```

## GPU Validation

Run host + Docker GPU checks:

```bash
./scripts/setup-gpu.sh
```

Or run directly in ai-worker container:

```bash
docker compose exec ai-worker nvidia-smi
```

## VS Code Dev Container

- Open the project in VS Code
- Run: `Dev Containers: Reopen in Container`
- The container uses `docker-compose.yml` and starts all services

## Notes

- This phase targets local development readiness and keeps architecture aligned with
  the modular monolith service boundaries.
- Cloud/K8s deployment is out of scope for Phase 0.
