# Policy Lifecycle & Data Coverage Notes

## 1. Policy Lifecycle Management (Updated)
- **2023 Policy (MOFCOM No. 39):** Natural Graphite (HS 250410/250490) - **Expired** (Ended Nov 30, 2024).
- **2024 Successor (MOFCOM No. 51):** Dual-use item control list (Code 1C108) - **Active** (From Dec 1, 2024).
- **2025 Policy (MOFCOM No. 58):** Artificial Graphite (HS 3801) - **Suspended** (Separate policy family, not applied to natural graphite).

## 2. KPI Logic Update
- The `v_kpi1_exposure` view now uses **date-matching logic** instead of just filtering by `status = 'Active'`. This ensures historical trade (e.g., 2023) is matched with the policy effective at that time (No. 39), and current trade (e.g., 2025) is matched with the successor policy (No. 51).

## 3. Data Coverage (2025)
- 2025 annual data is successfully ingested and mapped.
- **Caveat:** 2025 data is preliminary and subject to UN Comtrade revisions. It is labeled as "Latest Available Year".