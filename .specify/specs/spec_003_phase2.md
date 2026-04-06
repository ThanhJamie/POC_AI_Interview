# SPEC-003: Phase 2 - Realtime WebSocket + Session Management
**Version:** 1.0
**Phase:** 2
**Objective:** Xây dựng WebSocket endpoint nhận audio chunk realtime và quản lý session.

**Acceptance Criteria:**
- WS endpoint /ws/interview/{session_id} kết nối thành công
- Xử lý 3 message type (audio_chunk, transcript, assistant_response)
- Redis lưu session state
- Ping/pong + rate limiting

**Deliverables:**
- routers/ws/interview.py
- services/websocket_manager.py
- models/ws_message.py

**Constraints:**
- Async WebSocket
- JSON message format chuẩn
- Không lưu audio raw

**Implementation Plan:**
1. Tạo WebSocket router
2. Viết WebSocketManager class
3. Xử lý message type
4. Tích hợp Redis
5. Thêm ping/pong

**Test Cases:**
- Kết nối WS từ browser (Postman hoặc frontend test)
- Gửi audio_chunk → nhận echo
- Session tồn tại sau reconnect

**Next Phase Trigger:** SPEC-004.