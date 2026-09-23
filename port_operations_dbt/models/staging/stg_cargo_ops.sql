SELECT move_id,
       container_id,
       vessel_call_id,
       UPPER(TRIM(move_type)) AS move_type,
       event_time,
       crane_id,
       container_size,
       weight_kg
FROM {{source('port_ops', 'cargo_ops_raw')}}