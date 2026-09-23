SELECT *
FROM {{ref('mart_vessel_performance')}}
WHERE total_moves <> load_moves + discharge_moves