# SPEC-002: Phase 1 - Backend Foundation + Database
**Version:** 1.0
**Phase:** 1
**Objective:** Xây dựng FastAPI core, models SQLModel, kết nối PostgreSQL + pgvector, Alembic migration sẵn sàng.

**Acceptance Criteria:**
- Backend chạy port 8000, Swagger /docs hoạt động
- Alembic init + migration thành công
- pgvector extension được kích hoạt
- CRUD Interview cơ bản (create, read)
- Kết nối Redis thành công

**Deliverables:**
- app/models/ (Interview, Message, Embedding)
- app/database.py + engine
- app/routers/interview.py (CRUD)
- alembic/ folder + migrations
- alembic.ini
- requirements.txt cập nhật (sqlmodel, alembic, psycopg2, redis)

**Constraints:**
- Pydantic v2 + SQLModel
- Database URL từ .env
- UUID + TIMESTAMPTZ

**Implementation Plan:**
1. Cài dependencies
2. Tạo models + database engine
3. Cấu hình Alembic
4. Viết init.sql + migration đầu tiên
5. Tạo CRUD router
6. Test Swagger

**Test Cases:**
- POST /interviews tạo record thành công
- Kiểm tra pgvector extension trong DB
- alembic upgrade head không lỗi

**Next Phase Trigger:** Khi backend + DB chạy ổn → SPEC-003.