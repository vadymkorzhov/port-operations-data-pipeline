SELECT vessel_call_id,
        imo,
        vessel_name,
        service,
        terminal,
        berth,
        eta,
        etd,
        UPPER(TRIM(status)) AS status,
        updated_at
FROM {{source('port_ops', 'vessel_raw')}}