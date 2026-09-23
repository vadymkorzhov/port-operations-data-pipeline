{{ config(materialized='table') }}

WITH cargo_ops AS(
SELECT
    vessel_call_id,
    SUM(weight_kg) AS total_cargo_weight_kg
FROM {{ref('stg_cargo_ops')}}
GROUP BY vessel_call_id),
berth_ops AS(
SELECT
    vessel_call_id,
    ROUND(SUM(EXTRACT(EPOCH FROM (actual_end - actual_start)) / 3600), 1) AS total_berth_hours
FROM {{ref('stg_berth_ops')}}
GROUP BY vessel_call_id)
SELECT
    v.terminal,
     COUNT(v.vessel_call_id) AS vessel_calls,
    COALESCE(SUM(b.total_berth_hours), 0) AS total_berth_hours,
    COALESCE(SUM(c.total_cargo_weight_kg), 0) AS total_cargo_weight_kg
FROM {{ref('stg_vessel')}} v
LEFT JOIN cargo_ops c
    ON v.vessel_call_id = c.vessel_call_id
LEFT JOIN berth_ops b
    ON v.vessel_call_id = b.vessel_call_id
GROUP BY terminal