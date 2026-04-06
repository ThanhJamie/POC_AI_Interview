# SPEC-004: Phase 3 - STT + VAD
**Version:** 1.0
**Phase:** 3
**Objective:** Xử lý audio chunk realtime với faster-whisper large-v3 + silero-vad.

**Acceptance Criteria:**
- Chunk 1.5s → transcript + confidence < 1s
- VAD detect “ngừng nói” chính xác ≥ 95%
- Fallback khi GPU crash (log + error)

**Deliverables:**
- ai-worker/app/stt.py
- ai-worker/app/vad.py
- endpoint /stt/process_chunk

**Constraints:**
- CUDA 12.4
- faster-whisper large-v3
- silero-vad onnx

**Implementation Plan:**
1. Load model + VAD
2. Viết process_chunk async
3. Thêm VAD threshold
4. Tích hợp với backend WS

**Test Cases:**
- Gửi audio mock 2s → nhận transcript tiếng Việt
- VAD detect pause đúng

**Next Phase Trigger:** SPEC-005.