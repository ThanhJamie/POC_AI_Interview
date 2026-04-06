# SPEC-008: Phase 7 - Frontend UI + Audio Experience
**Version:** 1.0
**Phase:** 7
**Objective:** Xây dựng Next.js 15 UI đẹp, AudioRecorder + Waveform realtime.

**Acceptance Criteria:**
- Upload CV/JD → RAG
- Waveform nhảy theo giọng nói
- Live transcript + auto play audio

**Deliverables:**
- app/interview/page.tsx
- components/AudioRecorder.tsx + Waveform.tsx
- Zustand store

**Constraints:**
- MediaRecorder API
- shadcn/ui + Tailwind

**Implementation Plan:**
1. Next.js App Router
2. MediaRecorder + WS
3. Waveform component
4. Upload + RAG preview

**Test Cases:**
- Ghi âm → waveform realtime
- Audio play mượt

**Next Phase Trigger:** SPEC-009.