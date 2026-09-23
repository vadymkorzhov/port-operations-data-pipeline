SELECT *
FROM {{ ref('mart_berth_performance') }}
WHERE vessels < 0 OR total_hours < 0 OR total_cargo_weight_kg < 0