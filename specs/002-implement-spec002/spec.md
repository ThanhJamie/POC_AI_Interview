# Feature Specification: Phase 1 Backend Foundation and Database

**Feature Branch**: `002-implement-spec002`  
**Created**: 2026-04-06  
**Status**: Draft  
**Input**: User description: "tiếp tục implement spec002"

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Initialize Backend API and Data Layer (Priority: P1)

As a backend developer, I need a running FastAPI service with persistent data models so that
interview sessions can be created and queried reliably.

**Why this priority**: This is the minimum functional backend baseline for all later realtime and
AI workflow phases.

**Independent Test**: Start backend and call create/read endpoints for interviews against PostgreSQL.

**Acceptance Scenarios**:

1. **Given** backend service is running, **When** a client posts interview payload,
   **Then** a persisted interview record with UUID and timestamps is returned.
2. **Given** an existing interview ID, **When** client requests it,
   **Then** backend returns matching interview entity or a not found response.

---

### User Story 2 - Enable Migration Workflow (Priority: P2)

As a maintainer, I need Alembic configuration and an initial migration so schema changes can be
versioned and applied consistently.

**Why this priority**: Schema version control is required before introducing additional entities in later phases.

**Independent Test**: Run `alembic upgrade head` and verify expected tables are created.

**Acceptance Scenarios**:

1. **Given** a clean database, **When** migrations are executed,
   **Then** schema is created without manual SQL edits.

---

### User Story 3 - Validate Service Dependencies (Priority: P3)

As an operator, I need backend dependency checks for PostgreSQL and Redis so service readiness is visible.

**Why this priority**: Ensures runtime environment quality before Phase 2 realtime work.

**Independent Test**: Call health and dependency endpoints to verify DB and Redis connectivity.

**Acceptance Scenarios**:

1. **Given** backend dependencies are reachable, **When** dependency check endpoint is called,
   **Then** status indicates healthy for both PostgreSQL and Redis.

---

### Edge Cases

- Database container is up but credentials in environment are invalid.
- Redis is unavailable while DB is healthy.
- Create interview request misses required fields.
- Migration runs twice and must remain idempotent where appropriate.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Backend service MUST run on port 8000 and expose OpenAPI docs at `/docs`.
- **FR-002**: Backend MUST define SQLModel entities for Interview, Message, and Embedding.
- **FR-003**: Backend MUST create SQLAlchemy/SQLModel engine using database URL from environment.
- **FR-004**: Backend MUST expose interview create/read endpoints with UUID identifiers.
- **FR-005**: Backend MUST provide Alembic configuration and initial migration artifacts.
- **FR-006**: Backend MUST verify PostgreSQL connectivity through runtime check endpoint.
- **FR-007**: Backend MUST verify Redis connectivity through runtime check endpoint.
- **FR-008**: Entities MUST include timezone-aware timestamps for creation/update tracking.

### Constitution Alignment Requirements *(mandatory)*

- **CA-001**: Scope remains within backend and database services, preserving modular monolith boundaries.
- **CA-002**: AI inference responsibilities remain in ai-worker and are not introduced in this phase.
- **CA-003**: Data model and API contracts remain compatible with upcoming realtime/WebSocket phases.
- **CA-004**: Engineering standards follow Pydantic v2 type safety, Ruff, and consistent formatting.
- **CA-005**: Work is constrained to roadmap Phase 1 and prepares trigger conditions for Phase 2.

### Key Entities *(include if feature involves data)*

- **Interview**: Interview session root entity with ID, candidate context, status, and timestamps.
- **Message**: Conversation unit linked to an Interview and role (`candidate`, `assistant`, `system`).
- **Embedding**: Vector metadata linked to source content and interview scope for retrieval support.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `POST /interviews` and `GET /interviews/{id}` succeed for valid payloads.
- **SC-002**: `alembic upgrade head` completes without errors on clean database.
- **SC-003**: Dependency endpoint reports healthy DB and Redis in normal runtime state.
- **SC-004**: Swagger UI (`/docs`) is available when backend service starts.
- **SC-005**: Data entities include UUID primary keys and timezone-aware timestamps.

## Assumptions

- PostgreSQL and Redis services from Phase 0 are available via Docker Compose.
- `db/init.sql` already enables required DB extensions (`vector`, `uuid-ossp`).
- Authentication and authorization remain out of scope for this phase.
