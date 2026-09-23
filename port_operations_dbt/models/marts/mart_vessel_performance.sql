{{ config(materialized='table') }}

WITH cargo_ops AS (
SELECT
    vessel_call_id,
     COUNT(*) AS total_moves,
     SUM(weight_kg) AS total_cargo_weight_kg,
        SUM (
            CASE
                 WHEN move_type = 'LOAD' THEN 1
                 ELSE 0
                 END) AS load_moves,
        SUM (
            CASE
                WHEN move_type = 'DISCHARGE' THEN 1
                ELSE 0
                END) AS discharge_moves

FROM {{ref('stg_cargo_ops')}}
GROUP BY vessel_call_id),
berth_ops AS(
SELECT
    vessel_call_id,
    ROUND(SUM(EXTRACT(EPOCH FROM (planned_end - planned_start)) / 3600), 1) AS planned_ops_hours,
    ROUND(SUM(EXTRACT(EPOCH FROM (actual_end - actual_start)) / 3600),1) AS actual_ops_hours,
    ROUND(EXTRACT(EPOCH FROM (MIN(actual_start) - MIN(planned_start)) / 3600),2) AS ops_delay_hours
FROM {{ref('stg_berth_ops')}}
GROUP BY vessel_call_id
)
SELECT
    v.vessel_call_id,
    v.vessel_name,
    v.terminal,
    v.berth,
    v.eta,
    v.etd,
    COALESCE(c.load_moves, 0) AS load_moves,
    COALESCE(c.discharge_moves, 0) AS discharge_moves,
    COALESCE(c.total_moves, 0) AS total_moves,
    COALESCE(c.total_cargo_weight_kg, 0) AS total_cargo_weight_kg,
    b.planned_ops_hours,
    b.actual_ops_hours,
    b.ops_delay_hours,
    ROUND(b.actual_ops_hours - b.planned_ops_hours,1) AS ops_overrun_hours
FROM {{ref('stg_vessel')}} v
LEFT JOIN cargo_ops c
    ON v.vessel_call_id = c.vessel_call_id
LEFT JOIN berth_ops b
    ON v.vessel_call_id = b.vessel_call_id
ORDER BY vessel_call_id


