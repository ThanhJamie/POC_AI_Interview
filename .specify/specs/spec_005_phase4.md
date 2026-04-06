# SPEC-005: Phase 4 - TTS Streaming
**Version:** 1.0
**Phase:** 4
**Objective:** Stream audio từ text ra browser realtime với Edge-TTS.

**Acceptance Criteria:**
- Text → mp3 chunk stream latency < 0.5s
- Tích hợp WS push audio
- Hỗ trợ tiếng Việt (voice HoaiMyNeural)

**Deliverables:**
- ai-worker/app/tts.py
- endpoint /tts/stream

**Constraints:**
- Streaming chunk (không buffer hết)
- mp3 format

**Implementation Plan:**
1. Edge-TTS Communicator
2. Async generator chunk
3. Tích hợp với orchestrator

**Test Cases:**
- Text dài 30 từ → audio phát mượt
- WS nhận được audio_chunk

**Next Phase Trigger:** SPEC-006.