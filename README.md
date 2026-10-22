# Geopolitical Exposure in Critical Mineral Trade
## Identifying Policy-Exposed Supplier Dependencies and Quantifying Trade-at-Risk Scenarios

### 📌 Project Overview
This project quantifies the exposure of critical mineral supply chains to geopolitical policies (specifically export restrictions). It connects trade flows with documented policy interventions to measure "Potential Exposure" and simulates "Trade-at-Risk" scenarios.

**Policy Use Case:** China imposed Export Licensing on specific graphite items (HS 250410, 250490) starting December 1, 2023. This project measures which importers (e.g., South Korea, USA, Germany) are most exposed to this policy.

### 📊 Data Sources
- **Trade Data:** UN Comtrade (via Project 1: EV Battery Supply Chain Intelligence).
- **Policy Data:** MOFCOM (China) Announcement 2023 No. 39 (hand-curated into `geo.dim_export_policy`).

### 🛠️ Technical Stack
- **Database:** PostgreSQL (Schemas: `ev` for trade, `geo` for policy).
- **ETL & Analysis:** Python (pandas, SQLAlchemy).
- **Visualization:** Power BI.

### 📈 Key Metrics (KPIs)
- **KPI 1 (Potential Exposure):** The share of imports from a source subject to a policy restriction.
- **KPI 3 (Trade-at-Risk):** The volume of trade directly disrupted under hypothetical export reduction scenarios (25%, 50%, 100%).
- **Observed Trade Volume:** Historical trade volume with alternative suppliers (not spare capacity).

### ⚠️ Known Limitations
- **Coverage Gap:** Our trade database covers specific trade partners; WITS includes all global partners. This causes minor discrepancies in the denominator.
- **Policy Scope:** China's policy applies to specific national tariff lines. We use HS6 as a proxy for Potential Exposure, not a definitive ban list.
- **Annual Data:** Trade data is annual. We cannot precisely align 6-month windows around the Dec 2023 policy.
- **Spare Capacity:** Historical trade volumes do not equal available spare capacity for alternative suppliers.