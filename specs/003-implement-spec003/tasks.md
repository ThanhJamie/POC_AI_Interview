# Tasks: Phase 2 Realtime WebSocket and Session Management

**Input**: Documents from `/specs/003-implement-spec003/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup

- [x] T001 Create websocket package structure (`app/routers/ws`, `app/services`, websocket model)
- [x] T002 Update backend dependencies if websocket/session support libs are missing

## Phase 2: Tests First

- [x] T003 Add websocket integration tests for connect + ping/pong
- [x] T004 Add websocket integration tests for message handling + reconnect state

## Phase 3: Core Implementation

- [x] T005 Implement typed websocket message model (`audio_chunk`, `transcript`, `assistant_response`)
- [x] T006 Implement websocket manager with rate limiting and session state operations
- [x] T007 Implement websocket interview router at `/ws/interview/{session_id}`
- [x] T008 Integrate websocket router into FastAPI app

## Phase 4: Integration

- [x] T009 Add Redis-backed session state persistence with reconnect recovery
- [x] T010 Ensure audio_chunk handling stores metadata only (no raw audio payload)
- [x] T011 Add structured error handling for invalid message type/JSON/rate limit

## Phase 5: Polish and Validation

- [x] T012 Run integration tests and static error checks
- [x] T013 Mark all tasks complete and summarize validation outputs

## Dependencies & Execution Order

- T001 -> T002 -> T003/T004
- T003/T004 -> T005 -> T006 -> T007 -> T008
- T008 -> T009 -> T010 -> T011
- T011 -> T012 -> T013
