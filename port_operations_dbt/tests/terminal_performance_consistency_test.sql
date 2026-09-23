SELECT *
FROM {{ref('mart_terminal_performance')}}
WHERE vessel_calls < 0 OR total_berth_hours < 0 OR total_cargo_weight_kg < 0