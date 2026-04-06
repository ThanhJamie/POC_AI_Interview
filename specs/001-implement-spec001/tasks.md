# Tasks: Phase 0 Initialization and Infrastructure

**Input**: Documents from `/specs/001-implement-spec001/`
**Prerequisites**: plan.md, spec.md
**Tests**: Runtime validation commands are included.

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Create base folder structure for services and infrastructure files
- [X] T002 Add Docker Compose with five services and dependency graph
- [X] T003 [P] Add Dockerfiles for frontend, backend, and ai-worker

## Phase 2: Constitution-Driven Foundations (Blocking)

- [X] T004 Add database bootstrap SQL with pgvector and uuid-ossp extensions
- [X] T005 [P] Add `.env.example` with required runtime variables
- [X] T006 [P] Add `scripts/setup-gpu.sh` for GPU runtime checks
- [X] T007 Add Dev Container and VS Code settings for Ruff and Prettier

## Phase 3: Foundational (Blocking Prerequisites)

- [X] T008 Create backend dependency manifest and minimal app entrypoint
- [X] T009 Create ai-worker dependency manifest and minimal app entrypoint
- [X] T010 Create frontend `package.json` placeholder and metadata

## Phase 4: Validation and Documentation

- [X] T011 Add README with setup, run, and GPU validation steps
- [X] T012 Run structural validation for required files and service list

## Dependencies & Execution Order

- T001 -> T002/T003
- T002/T003 -> T004/T005/T006/T007
- T004/T005/T006/T007 -> T008/T009/T010
- T008/T009/T010 -> T011 -> T012
