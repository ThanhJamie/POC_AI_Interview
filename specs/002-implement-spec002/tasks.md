# Tasks: Phase 1 Backend Foundation and Database

**Input**: Documents from `/specs/002-implement-spec002/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup

- [X] T001 Create backend package structure for models, schemas, routers, and db config
- [X] T002 Update backend dependencies for pgvector support and migration tooling

## Phase 2: Tests First

- [X] T003 Add API contract smoke tests for interview create/read behavior
- [X] T004 Add migration smoke check script for `alembic upgrade head`

## Phase 3: Core Implementation

- [X] T005 Implement settings and database engine/session management
- [X] T006 Implement SQLModel entities (Interview, Message, Embedding)
- [X] T007 Implement interview schemas and CRUD router
- [X] T008 Integrate router into FastAPI app and add dependency health endpoint

## Phase 4: Integration

- [X] T009 Add Alembic configuration files and initial migration script
- [X] T010 Ensure db init SQL and app startup are consistent with pgvector + uuid-ossp
- [X] T011 Validate Redis connectivity through backend dependency checks

## Phase 5: Polish and Validation

- [X] T012 Run syntax/error checks and fix issues
- [X] T013 Mark completed tasks and summarize validation evidence

## Dependencies & Execution Order

- T001 -> T002 -> T003/T004
- T003/T004 -> T005 -> T006 -> T007 -> T008
- T008 -> T009 -> T010 -> T011
- T011 -> T012 -> T013
