# SPEC-007: Phase 6 - Full Realtime Interview Loop
**Version:** 1.0
**Phase:** 6
**Objective:** Kết nối toàn bộ STT → LangGraph → TTS thành vòng lặp realtime.

**Acceptance Criteria:**
- End-to-end latency < 3 giây
- Early TTS (first sentence)
- Lưu message + audio URL vào DB

**Deliverables:**
- backend/app/services/interview_orchestrator.py
- Conditional routing đầy đủ

**Constraints:**
- VAD trigger gọi Agent
- Stream response

**Implementation Plan:**
1. Orchestrator class
2. Kết nối WS + AI Worker
3. Early response logic
4. DB logging

**Test Cases:**
- Full 1 vòng (nói → AI trả lời) mượt
- Transcript lưu đúng

**Next Phase Trigger:** SPEC-008.