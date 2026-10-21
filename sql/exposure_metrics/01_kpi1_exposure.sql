CREATE OR REPLACE VIEW geo.v_kpi1_exposure AS
WITH policy_exposed_trade AS (
    -- 1. تجارت‌هایی که تحت تاثیر مستقیم سیاست هستند
    SELECT
        t.date_id,
        d.year,
        t.importer_country_id,
        importer.country_name AS importer_name,
        t.hs_code,
        p.policy_type,
        SUM(t.trade_quantity) AS exposed_qty
    FROM ev.fact_trade t
    JOIN ev.dim_date d ON d.date_id = t.date_id
    JOIN ev.dim_country importer ON importer.country_id = t.importer_country_id
    JOIN ev.dim_country exporter ON exporter.country_id = t.exporter_country_id
    JOIN geo.dim_export_policy p ON p.hs_code = t.hs_code AND exporter.country_code = p.implementing_country_code
    WHERE t.flow_code = 'M'
      AND d.year >= EXTRACT(YEAR FROM p.start_date) -- فقط بعد از شروع سیاست
    GROUP BY t.date_id, d.year, t.importer_country_id, importer.country_name, t.hs_code, p.policy_type
),
total_trade AS (
    -- 2. کل واردات هر کشور (بدون توجه به سیاست)
    SELECT
        t.date_id,
        t.importer_country_id,
        t.hs_code,
        SUM(t.trade_quantity) AS total_qty
    FROM ev.fact_trade t
    WHERE t.flow_code = 'M'
    GROUP BY t.date_id, t.importer_country_id, t.hs_code
)
SELECT
    e.year,
    e.importer_name,
    e.hs_code,
    e.policy_type,
    ROUND(e.exposed_qty::numeric, 2) AS exposed_qty_t,
    ROUND(tot.total_qty::numeric, 2) AS total_qty_t,
    ROUND((e.exposed_qty / tot.total_qty * 100)::numeric, 2) AS exposure_share_pct
FROM policy_exposed_trade e
JOIN total_trade tot 
  ON e.date_id = tot.date_id 
 AND e.importer_country_id = tot.importer_country_id 
 AND e.hs_code = tot.hs_code
ORDER BY e.year DESC, exposure_share_pct DESC;