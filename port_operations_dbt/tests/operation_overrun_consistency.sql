SELECT *
FROM {{ref('mart_vessel_performance')}}
WHERE actual_ops_hours IS NULL AND ops_overrun_hours IS NOT NULL