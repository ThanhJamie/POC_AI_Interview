# Implementation Plan: WebSocket Session Management

**Branch**: `003-implement-spec003` | **Date**: 2026-04-06 | **Spec**: [/home/thanh/home/thanh/project/ai-interview-poc/specs/003-implement-spec003/spec.md](/home/thanh/home/thanh/project/ai-interview-poc/specs/003-implement-spec003/spec.md)
**Input**: Feature specification from `/specs/003-implement-spec003/spec.md`

## Summary

Implement a production-safe WebSocket session layer for interview streaming on the backend with typed message envelopes, ping/pong liveness checks, per-session rate limiting, and reconnect state recovery. The delivery includes:

- Typed protocol models for client/server messages.
- A `WebSocketManager` service with Redis-backed session state and in-memory fallback.
- A FastAPI WebSocket endpoint at `/ws/interview/{session_id}`.
- Integration tests for happy path, reconnect behavior, and throttling.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: FastAPI, SQLModel, Redis (async), Pydantic v2
**Storage**: PostgreSQL (existing), Redis for session cache (with memory fallback)
**Testing**: Pytest (`backend/tests/integration/test_ws_interview.py`)
**Target Platform**: Docker Compose local stack (Linux containers)
**Project Type**: Backend service in modular monolith
**Performance Goals**:

- Session keepalive supports sub-second ping/pong handling at app layer.
- Reconnect restores latest persisted session state for continuity.
- Enforce configurable burst/window message limits to protect service.
  **Constraints**:
- Preserve modular-monolith boundaries from constitution.
- Keep protocol and session logic server-side only (no AI inference in backend WS loop).
- Maintain deterministic JSON error responses for invalid payloads.
  **Scale/Scope**:
- Single interview room per `session_id`.
- Designed for PoC concurrency with guardrails and future horizontal scaling via Redis.

## Constitution Check

_GATE: Must pass before Phase 0 research. Re-check after Phase 1 design._

- **Modular Monolith Boundary**: PASS
  - WS logic implemented in backend service modules (`models`, `services`, `routers`) without cross-service coupling.
- **AI Worker Separation**: PASS
  - Endpoint handles signaling/session orchestration only; no model inference logic added.
- **Realtime Pipeline and Latency Discipline**: PASS
  - Ping/pong, strict typed envelopes, and rate limiting integrated to maintain predictable realtime behavior.
- **Fixed Stack Compliance**: PASS
  - Uses FastAPI/Python + Redis + existing Postgres stack only.
- **Vietnamese-First UX Contract**: N/A (backend transport feature)
- **Developer Experience and Quality Gates**: PASS
  - Integration tests added and executed successfully.

## Project Structure

### Documentation (this feature)

```text
specs/003-implement-spec003/
|- plan.md
|- spec.md
`- tasks.md
```

### Source Code (implemented)

```text
backend/
|- app/
|  |- config.py
|  |- main.py
|  |- models/
|  |  |- __init__.py
|  |  `- ws_message.py
|  |- routers/
|  |  |- __init__.py
|  |  `- ws/
|  |     |- __init__.py
|  |     `- interview.py
|  `- services/
|     |- __init__.py
|     `- websocket_manager.py
`- tests/
   `- integration/
      `- test_ws_interview.py
```

**Structure Decision**: Keep protocol contracts in `models`, orchestration/state handling in `services`, and transport endpoint in `routers/ws` to preserve separations and testability.

## Phase Execution Summary

### Phase 1: Protocol and Session Service

- Added typed message models in `ws_message.py`.
- Implemented `WebSocketManager` for:
  - Connection tracking per `session_id`.
  - Redis state save/load with memory fallback.
  - Session-aware rate limiting.
  - Message handling for `audio_chunk`, `transcript`, `assistant_response`, `ping`.

### Phase 2: WebSocket Router Integration

- Added `/ws/interview/{session_id}` endpoint.
- Added JSON parsing + schema validation + structured error envelopes.
- Connected lifecycle events to manager (`connect`, `handle_message`, `disconnect`).
- Registered WS router in `main.py`.

### Phase 3: Verification

- Added integration tests for:
  - Connection acknowledgement.
  - Ping/pong response.
  - Invalid payload handling.
  - Reconnect state recovery.
  - Rate limiting behavior.
- Test status: passing (`5 passed`).

## Risk and Mitigation

- **Redis unavailable in local/dev**:
  - Mitigation: in-memory fallback keeps tests/dev flow operational.
- **Client sends malformed JSON or unsupported type**:
  - Mitigation: centralized schema validation and explicit error envelopes.
- **Burst traffic on a single session**:
  - Mitigation: per-session rate-limiter with configurable thresholds.

## Completion Notes

This feature scope is implemented and validated against the associated task list in [/home/thanh/home/thanh/project/ai-interview-poc/specs/003-implement-spec003/tasks.md](/home/thanh/home/thanh/project/ai-interview-poc/specs/003-implement-spec003/tasks.md). The plan is updated to reflect actual implementation details for phase handoff and auditability.
