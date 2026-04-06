# SPEC-009: Phase 8 - Testing, Polish & Production Readiness
**Version:** 1.0
**Phase:** 8
**Objective:** Hoàn thiện test, báo cáo cuối phiên, Helm chart, production migration guide.

**Acceptance Criteria:**
- Full 15 phút interview mượt (latency < 3s)
- Unit test > 80%, E2E test
- Helm chart deploy được
- Báo cáo PDF/JSON

**Deliverables:**
- tests/ (pytest + Playwright)
- k8s/helm-chart/
- components/Report.tsx
- production-guide.md

**Constraints:**
- Performance tuning
- Fallback API

**Implementation Plan:**
1. Viết unit + E2E test
2. Tạo báo cáo UI
3. Viết Helm chart
4. Tuning latency

**Test Cases:**
- Chạy full interview 15 phút
- helm install test thành công

**Next Phase Trigger:** Production migration (Cloud/K8s).