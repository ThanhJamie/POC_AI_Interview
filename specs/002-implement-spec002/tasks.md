# Tasks: Phase 1 Backend Foundation and Database

**Input**: Documents from `/specs/002-implement-spec002/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup

- [ ] T001 Create backend package structure for models, schemas, routers, and db config
- [ ] T002 Update backend dependencies for pgvector support and migration tooling

## Phase 2: Tests First

- [ ] T003 Add API contract smoke tests for interview create/read behavior
- [ ] T004 Add migration smoke check script for `alembic upgrade head`

## Phase 3: Core Implementation

- [ ] T005 Implement settings and database engine/session management
- [ ] T006 Implement SQLModel entities (Interview, Message, Embedding)
- [ ] T007 Implement interview schemas and CRUD router
- [ ] T008 Integrate router into FastAPI app and add dependency health endpoint

## Phase 4: Integration

- [ ] T009 Add Alembic configuration files and initial migration script
- [ ] T010 Ensure db init SQL and app startup are consistent with pgvector + uuid-ossp
- [ ] T011 Validate Redis connectivity through backend dependency checks

## Phase 5: Polish and Validation

- [ ] T012 Run syntax/error checks and fix issues
- [ ] T013 Mark completed tasks and summarize validation evidence

## Dependencies & Execution Order

- T001 -> T002 -> T003/T004
- T003/T004 -> T005 -> T006 -> T007 -> T008
- T008 -> T009 -> T010 -> T011
- T011 -> T012 -> T013
