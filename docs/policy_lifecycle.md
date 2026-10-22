# Policy Lifecycle & Data Coverage Notes

## 1. Policy Lifecycle Management
- The `geo.dim_export_policy` table now tracks `status` (Active, Suspended) and `status_as_of`.
- **2023 Policy (MOFCOM No. 39):** Natural Graphite (HS 250410/250490) - **Active**.
- **2025 Policy (MOFCOM No. 58):** Artificial Graphite (HS 3801) - **Suspended** (from Nov 2025 to Nov 2026).
- **Critical Rule:** The KPI engine only joins with policies where `status = 'Active'`. This prevents artificial graphite (HS 3801) from affecting natural graphite (HS 2504) exposure metrics.

## 2. Data Coverage (2025)
- 2025 annual data is available in UN Comtrade and has been ingested.
- **Caveat:** 2025 data may be preliminary and subject to revision. It is treated as a current indicator, not a finalized historical year.
- **Future Work:** Monthly 2026 data ingestion (freqCode=M) is planned for continuous monitoring but is outside the scope of this phase.