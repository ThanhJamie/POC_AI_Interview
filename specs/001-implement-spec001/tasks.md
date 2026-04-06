# Tasks: Phase 0 Initialization and Infrastructure

**Input**: Documents from `/specs/001-implement-spec001/`
**Prerequisites**: plan.md, spec.md
**Tests**: Runtime validation commands are included.

## Phase 1: Setup (Shared Infrastructure)

- [x] T001 Create base folder structure for services and infrastructure files
- [x] T002 Add Docker Compose with five services and dependency graph
- [x] T003 [P] Add Dockerfiles for frontend, backend, and ai-worker

## Phase 2: Constitution-Driven Foundations (Blocking)

- [x] T004 Add database bootstrap SQL with pgvector and uuid-ossp extensions
- [x] T005 [P] Add `.env.example` with required runtime variables
- [x] T006 [P] Add `scripts/setup-gpu.sh` for GPU runtime checks
- [x] T007 Add Dev Container and VS Code settings for Ruff and Prettier

## Phase 3: Foundational (Blocking Prerequisites)

- [x] T008 Create backend dependency manifest and minimal app entrypoint
- [x] T009 Create ai-worker dependency manifest and minimal app entrypoint
- [x] T010 Create frontend `package.json` placeholder and metadata

## Phase 4: Validation and Documentation

- [x] T011 Add README with setup, run, and GPU validation steps
- [x] T012 Run structural validation for required files and service list

## Dependencies & Execution Order

- T001 -> T002/T003
- T002/T003 -> T004/T005/T006/T007
- T004/T005/T006/T007 -> T008/T009/T010
- T008/T009/T010 -> T011 -> T012
