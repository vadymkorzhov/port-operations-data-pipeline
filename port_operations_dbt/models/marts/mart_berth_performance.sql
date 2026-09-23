{{ config(materialized='table') }}

WITH berth_hours AS (
    SELECT
        vessel_call_id,
        berth_id,
        ROUND(SUM(EXTRACT(EPOCH FROM (actual_end - actual_start)) / 3600),1 ) AS total_hours
    FROM {{ref('stg_berth_ops')}}
    GROUP BY berth_id, vessel_call_id
),
cargo_ops AS (
    SELECT
        vessel_call_id,
        SUM(weight_kg) AS total_cargo_weight_kg
    FROM {{ref('stg_cargo_ops')}}
    GROUP BY vessel_call_id
)
SELECT
    b.berth_id,
    COUNT(b.vessel_call_id) AS vessels,
    SUM(b.total_hours) AS total_hours,
    SUM(c.total_cargo_weight_kg) AS total_cargo_weight_kg
FROM berth_hours b
LEFT JOIN cargo_ops c
    ON b.vessel_call_id = c.vessel_call_id
GROUP BY b.berth_id