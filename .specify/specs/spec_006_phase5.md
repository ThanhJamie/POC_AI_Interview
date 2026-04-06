# SPEC-006: Phase 5 - LangGraph Agent + RAG
**Version:** 1.0
**Phase:** 5
**Objective:** Xây dựng autonomous Interview Agent với LangGraph + RAG CV/JD.

**Acceptance Criteria:**
- State machine hoàn chỉnh (listen → reason → speak → evaluate)
- RAG similarity search top-5 từ pgvector
- Prompt interviewer nghiêm khắc + tiếng Việt

**Deliverables:**
- ai-worker/app/llm_agent.py
- ai-worker/app/rag_service.py
- InterviewState TypedDict

**Constraints:**
- Gemini embedding hoặc local sentence-transformers
- LangGraph checkpoint

**Implementation Plan:**
1. Định nghĩa InterviewState
2. Tạo nodes + edges
3. Viết RAG service
4. Prompt engineering

**Test Cases:**
- Agent tự hỏi tiếp theo logic
- RAG trả về chunk CV/JD đúng

**Next Phase Trigger:** SPEC-007.