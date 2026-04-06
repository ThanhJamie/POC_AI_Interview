<!--
Sync Impact Report
- Version change: template placeholder -> 1.0.0
- Modified principles:
	- Template Principle 1 -> I. Modular Monolith Architecture (4 Docker Services)
	- Template Principle 2 -> II. Scale-First AI Worker Separation
	- Template Principle 3 -> III. Realtime Interview Pipeline
	- Template Principle 4 -> IV. Fixed Technology Stack
	- Template Principle 5 -> V. Vietnamese-First Interaction
	- Added -> VI. End-to-End Latency Budget
	- Added -> VII. Engineering Standards and Tooling Discipline
- Added sections:
	- Operational Constraints
	- Mandatory Delivery Workflow
- Removed sections:
	- None
- Templates requiring updates:
	- ✅ .specify/templates/plan-template.md
	- ✅ .specify/templates/spec-template.md
	- ✅ .specify/templates/tasks-template.md
	- ⚠ pending: .specify/templates/commands/*.md (directory not present in repository)
	- ⚠ pending: README.md (file not present in repository)
	- ⚠ pending: docs/quickstart.md (file not present in repository)
- Deferred items:
	- None
-->

# AI Voice Interviewer PoC Constitution

## Core Principles

### I. Modular Monolith Architecture (4 Docker Services)
System MUST run as a modular monolith deployed with exactly four service containers:
frontend, backend, ai-worker, and db. All feature work MUST preserve this boundary and MUST
document any inter-service contract changes. Rationale: predictable operations and clear
ownership while preserving delivery speed for a PoC.

### II. Scale-First AI Worker Separation
AI inference and speech generation workloads MUST execute in ai-worker from day one and MUST
NOT be colocated with backend request handling. Backend MUST orchestrate, not perform, heavy
GPU-bound tasks. Rationale: isolates scaling and resource contention risks before traffic growth.

### III. Realtime Interview Pipeline
Realtime flow MUST use WebSocket transport, audio chunking at 1.5 seconds, VAD gating, and
early TTS emission. Any change to this chain MUST include latency impact assessment and rollback
strategy. Rationale: conversational quality depends on continuous low-latency turn-taking.

### IV. Fixed Technology Stack
The baseline stack is mandatory: Next.js 15, FastAPI, faster-whisper, LangGraph,
PostgreSQL with pgvector, and Edge-TTS. Replacing a core component MUST be proposed through a
constitution amendment with compatibility and migration evidence. Rationale: avoids churn and
keeps the team focused on product validation.

### V. Vietnamese-First Interaction
User-facing interview experience MUST prioritize Vietnamese and MUST provide English fallback.
Prompting, transcript handling, and response generation MUST define locale behavior explicitly.
Rationale: aligns with primary target users while preserving broader usability.

### VI. End-to-End Latency Budget
End-to-end interview turn latency MUST remain below 3 seconds for the primary interaction path.
Every feature affecting media, inference, or transport MUST include measurable latency criteria.
Rationale: latency is a product requirement, not an optimization backlog item.

### VII. Engineering Standards and Tooling Discipline
Python code MUST use Pydantic v2 models, type hints, and Ruff linting; web code and shared UI
artifacts MUST follow Prettier formatting. Pull requests MUST fail quality gates when standards
are violated. Rationale: consistent code quality enables safe rapid iteration.

## Operational Constraints

All implementation decisions MUST conform to the Phase Roadmap from Phase 0 through Phase 8.
Each spec, plan, and task set MUST declare the target phase and dependency on preceding phases.
Cross-phase shortcuts are prohibited unless a governance amendment explicitly allows them.

## Mandatory Delivery Workflow

Work MUST execute in this order without omission:
1. /specify to produce a complete feature specification.
2. /plan to confirm architecture and stack alignment.
3. /tasks to create dependency-ordered execution tasks.
4. /implement to generate code and tests from approved tasks.

Any pull request that bypasses this sequence MUST be blocked until artifacts are complete and
traceable to the approved phase.

## Governance

This constitution overrides conflicting local practices for this repository. Amendments require:
1. A documented proposal describing rationale, affected principles, and migration impact.
2. Approval from project maintainers responsible for backend, frontend, and AI worker domains.
3. Synchronization updates to templates and execution prompts before merge.

Versioning policy follows semantic versioning:
1. MAJOR for incompatible principle removals or redefinitions.
2. MINOR for new principles, new mandatory sections, or materially expanded obligations.
3. PATCH for clarifications and wording-only updates.

Compliance review expectations:
1. Every PR MUST include a constitution compliance checklist.
2. Reviews MUST verify architecture boundary, latency budget impact, language behavior, and
   workflow artifact completeness.
3. Quarterly governance review MUST confirm roadmap phase adherence and update controls if needed.

**Version**: 1.0.0 | **Ratified**: 2026-04-06 | **Last Amended**: 2026-04-06
