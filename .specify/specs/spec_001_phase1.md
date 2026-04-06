# SPEC-001: Phase 0 - Project Initialization & Infrastructure
**Version:** 1.1
**Phase:** 0
**Status:** Approved by Constitution
**Objective:** Xây dựng monorepo hoàn chỉnh, Docker Compose hỗ trợ GPU từ ngày đầu, Dev Container cho VS Code, môi trường chạy local 100% và sẵn sàng migrate sang Cloud/K8s mà không thay đổi cấu trúc.

**Acceptance Criteria:**
- docker-compose.yml chạy thành công 5 service (frontend, backend, ai-worker, db, redis)
- AI-Worker container nhận được GPU (nvidia-smi hiển thị đúng)
- Dev Container (.devcontainer) mở được VS Code bên trong Docker
- .env.example + README.md + .gitignore đầy đủ
- Không lỗi build, không phụ thuộc internet (trừ Docker pull)

**Deliverables:**
- docker-compose.yml (version 3.9, GPU reservation, depends_on)
- backend/Dockerfile, ai-worker/Dockerfile (nvidia/cuda base), frontend/Dockerfile (placeholder)
- db/init.sql (pgvector + uuid-ossp)
- .env.example (tất cả biến cần thiết)
- scripts/setup-gpu.sh
- README.md (hướng dẫn chạy + test GPU)
- .devcontainer/devcontainer.json
- .vscode/settings.json (Ruff + Prettier)
- backend/requirements.txt + ai-worker/requirements.txt + frontend/package.json

**Constraints:**
- Modular Monolith 4 service
- AI Worker tách GPU ngay từ Phase 0
- Python 3.12 + Node 20
- Không dùng Ollama/Gemini ở Phase này

**Implementation Plan:**
1. Tạo folder structure
2. Viết docker-compose.yml + GPU block
3. Viết 3 Dockerfile
4. Viết .env.example + init.sql
5. Viết script GPU + README
6. Viết .devcontainer + .vscode
7. Tạo requirements.txt placeholder
8. Test build & GPU

**Test Cases:**
- docker compose up --build -d thành công
- docker exec ai-worker nvidia-smi hiển thị GPU
- ./scripts/setup-gpu.sh chạy không lỗi
- VS Code Reopen in Container thành công

**Next Phase Trigger:** Khi tất cả Acceptance Criteria đạt → chuyển sang SPEC-002 (Phase 1).