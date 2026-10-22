# Data Validation & Reconciliation

This document addresses critical validations performed on the exposure and scenario metrics before visualization. Feedback from technical reviewers was incorporated to ensure data integrity and interpretative accuracy.

## 1. South Korea Exposure (KPI 1)
- **Observation:** Our KPI shows 98.95% potential exposure, while WITS/Comtrade shows ~97.22%.
- **Root Cause:** Our database covers a specific set of trade partners. WITS includes all global partners. The numerator (imports from China: 28,000.22t) matches WITS exactly. The denominator differs due to a **Coverage Gap** in our partner list.
- **Resolution:** The metric is renamed to `potential_exposure_pct`. The coverage limitation is documented.

## 2. USA Import Jump in HS 250490 (BQ2)
- **Observation:** A massive 20x jump was initially observed in 2024 (~19,867t).
- **Root Cause:** A double-counting error in the view `v_event_analysis`. We accidentally summed both the `REPORTED` (USA import) and `MIRROR` (China export) perspectives. 
- **Resolution:** The view was updated to strictly filter by `source_id = 'UN_COMTRADE_REPORTED'`. The corrected value is 9,933.57t, which now perfectly matches WITS.

## 3. Policy Scope (HS6 vs National Codes)
- **Observation:** China's export licensing applies to specific national tariff lines, not the entire HS 250490 category.
- **Resolution:** KPI is explicitly labeled as "Potential Exposure" based on a trade proxy. We do not claim it as a "100% export ban".

## 4. BQ4 (Alternative Suppliers)
- **Observation:** Historical trade volume does not equal spare capacity.
- **Resolution:** The column is renamed to `observed_trade_volume_t`. Reports will state that actual substitution requires unallocated capacity, which is outside Comtrade data.

## 5. Time Window Alignment & Intermediary Check
- **Time Alignment:** Due to the lack of monthly Comtrade data for these specific routes, the analysis uses annual aggregations (2023 vs 2024). Seasonality is a known limitation.
- **Intermediary Check:** Re-export flows (e.g., via Mexico or Vietnam) are not fully captured by bilateral Comtrade data for these HS codes. This is documented as a limitation.