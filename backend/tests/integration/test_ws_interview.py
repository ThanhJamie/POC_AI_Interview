import os

os.environ["DATABASE_URL"] = "sqlite:///./test_ws.db"
os.environ["REDIS_URL"] = "redis://localhost:6379/0"
os.environ["WS_RATE_LIMIT_MAX"] = "3"
os.environ["WS_RATE_LIMIT_WINDOW_SECONDS"] = "60"

from fastapi.testclient import TestClient

from app.main import app
from app.routers.ws.interview import manager


def test_ws_ping_pong() -> None:
    with TestClient(app) as client:
        with client.websocket_connect("/ws/interview/session-ping") as ws:
            first = ws.receive_json()
            assert first["type"] == "connection_ack"

            ws.send_json({"type": "ping", "payload": {}, "timestamp": "2026-04-06T00:00:00Z"})
            pong = ws.receive_json()
            assert pong["type"] == "pong"


def test_ws_audio_chunk_ack_and_reconnect_state() -> None:
    session_id = "session-reconnect"

    with TestClient(app) as client:
        with client.websocket_connect(f"/ws/interview/{session_id}") as ws:
            ws.receive_json()
            ws.send_json(
                {
                    "type": "audio_chunk",
                    "timestamp": "2026-04-06T00:00:00Z",
                    "payload": {
                        "chunk_index": 1,
                        "duration_ms": 1500,
                        "audio_base64": "QUJD",
                    },
                }
            )
            ack = ws.receive_json()
            assert ack["type"] == "audio_chunk_ack"
            assert ack["payload"]["stored"] == "metadata_only"
            assert ack["payload"]["state"]["audio_chunk_count"] >= 1

        with client.websocket_connect(f"/ws/interview/{session_id}") as ws2:
            reconnect = ws2.receive_json()
            assert reconnect["type"] == "connection_ack"
            assert reconnect["payload"]["state"]["audio_chunk_count"] >= 1


def test_ws_rate_limit_error() -> None:
    previous_limit = manager.rate_limit_max
    try:
        manager.rate_limit_max = 3
        manager._rate_windows.pop("session-rate", None)

        with TestClient(app) as client:
            with client.websocket_connect("/ws/interview/session-rate") as ws:
                ws.receive_json()
                ws.send_json({"type": "transcript", "payload": {"segment_id": 1}})
                ws.receive_json()
                ws.send_json({"type": "transcript", "payload": {"segment_id": 2}})
                ws.receive_json()
                ws.send_json({"type": "transcript", "payload": {"segment_id": 3}})
                ws.receive_json()

                # This message exceeds WS_RATE_LIMIT_MAX=3 and should return an error.
                ws.send_json({"type": "transcript", "payload": {"segment_id": 4}})
                error = ws.receive_json()
                assert error["type"] == "error"
                assert error["payload"]["code"] == "rate_limited"
    finally:
        manager.rate_limit_max = previous_limit
