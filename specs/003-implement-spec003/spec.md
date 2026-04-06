# Feature Specification: Phase 2 Realtime WebSocket and Session Management

**Feature Branch**: `003-implement-spec003`  
**Created**: 2026-04-06  
**Status**: Draft  
**Input**: User description: "tiếp tục spec 003"

## User Scenarios & Testing _(mandatory)_

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

### User Story 1 - Establish Realtime Session Channel (Priority: P1)

As an interview client, I need to open a stable websocket session channel so realtime interview
messages can be exchanged continuously.

**Why this priority**: Realtime transport is required before STT/TTS orchestration phases.

**Independent Test**: Connect to `/ws/interview/{session_id}` and exchange ping/pong + structured messages.

**Acceptance Scenarios**:

1. **Given** a valid session id, **When** client connects websocket,
   **Then** server acknowledges connection and initializes session state.
2. **Given** an open websocket, **When** client sends `ping`,
   **Then** server responds with `pong` without closing the session.

---

### User Story 2 - Handle Interview Message Types (Priority: P2)

As backend realtime infrastructure, I need to process the three core message types
(`audio_chunk`, `transcript`, `assistant_response`) using a consistent JSON envelope.

**Why this priority**: This defines the transport contract used by downstream AI pipeline stages.

**Independent Test**: Send each message type and verify deterministic server acknowledgement payloads.

**Acceptance Scenarios**:

1. **Given** a connected session, **When** client sends `audio_chunk`,
   **Then** server acknowledges chunk metadata and does not persist raw audio payload.
2. **Given** a connected session, **When** client sends `transcript` or `assistant_response`,
   **Then** server updates session state and returns acknowledgement.

---

### User Story 3 - Persist and Recover Session State (Priority: P3)

As a session service, I need to keep realtime session state in Redis and support reconnect
continuity so temporary disconnects do not reset interview flow.

**Why this priority**: Session continuity is required for robust realtime UX in unstable networks.

**Independent Test**: Disconnect and reconnect using same `session_id`, verify counters/state survive.

**Acceptance Scenarios**:

1. **Given** prior websocket activity for a session, **When** client reconnects,
   **Then** server reloads session state from storage and continues sequence tracking.

---

### Edge Cases

- Client sends malformed JSON payload.
- Client sends unsupported `type` value.
- Client exceeds allowed message rate.
- Redis becomes temporarily unavailable during session updates.
- Client reconnects with same session_id while another socket is still open.

## Requirements _(mandatory)_

### Functional Requirements

- **FR-001**: Backend MUST expose websocket endpoint `/ws/interview/{session_id}`.
- **FR-002**: Websocket message envelope MUST include `type`, `timestamp`, and `payload`.
- **FR-003**: Backend MUST process `audio_chunk`, `transcript`, and `assistant_response` message types.
- **FR-004**: Backend MUST store per-session realtime state in Redis.
- **FR-005**: Backend MUST implement ping/pong handling for liveness checks.
- **FR-006**: Backend MUST enforce per-session message rate limiting.
- **FR-007**: Backend MUST reject unsupported message types with structured error responses.
- **FR-008**: Backend MUST not persist raw audio data from `audio_chunk` payloads.
- **FR-009**: Backend MUST recover session state on reconnect using `session_id`.

### Constitution Alignment Requirements _(mandatory)_

- **CA-001**: Scope remains within backend realtime transport and Redis session storage only.
- **CA-002**: WebSocket transport behavior aligns with mandated realtime pipeline prerequisites.
- **CA-003**: Message format remains compatible with Vietnamese-first interview workflow in later phases.
- **CA-004**: Session and transport design supports downstream latency objectives (<3s end-to-end).
- **CA-005**: Work is constrained to roadmap Phase 2 and prepares trigger for SPEC-004.

### Key Entities _(include if feature involves data)_

- **WSMessage**: Normalized websocket payload with type, timestamp, and typed body.
- **InterviewSessionState**: Session metadata stored in Redis (message counts, last activity, reconnect info).
- **RateLimitWindow**: Per-session rolling timestamps used to throttle message intake.

## Success Criteria _(mandatory)_

### Measurable Outcomes

- **SC-001**: Websocket connection to `/ws/interview/{session_id}` succeeds in smoke tests.
- **SC-002**: All three message types return successful structured acknowledgements.
- **SC-003**: Ping request returns pong response within same websocket session.
- **SC-004**: Reconnect with same session_id restores message counters/state.
- **SC-005**: Rate limiter blocks excess traffic with explicit error response.

## Assumptions

- Backend foundation and data models from SPEC-002 are available.
- Redis service is reachable in docker compose runtime.
- Authentication remains out of scope for this phase.
- Raw audio binary handling is deferred to ai-worker pipeline phases.
