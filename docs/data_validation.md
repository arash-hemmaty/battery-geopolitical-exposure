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

## 6. Advanced Validations (Stage 3)

### Intermediary Check (Mexico/Vietnam Bypass)
- **Test:** Checked if Mexico imports from China and re-exports to the US (HS 250490).
- **Result:** No evidence of significant re-export flows. Mexico's imports from China are negligible, and its exports to the US are very small (~200-800t). The hypothesis of bypassing restrictions via Mexico is rejected for this dataset.

### Unbalanced Panel Check
- **Test:** Checked for missing years (nulls) vs zero imports for DEU, KOR, USA (2021-2025).
- **Result:** All three countries have continuous observations across all years. The panel is balanced. No missing data was mistakenly treated as zero trade.

### Time Window Alignment (Limitation)
- **Test:** Aligning 6-month windows before/after Dec 2023.
- **Result:** The ingested Comtrade data is annual (A). Monthly data is not available in our current dataset. The Event Analysis remains at the annual level (2023 vs 2024). Seasonality is a documented limitation.

## 7. Country-Specific Context (Germany)
- **Rotterdam Effect:** Germany's imports of graphite may enter through EU ports (e.g., Rotterdam in the Netherlands or Antwerp in Belgium). Bilateral Comtrade data might not fully capture intra-EU re-exports. The actual direct dependency of Germany on China could be slightly lower or higher than measured.