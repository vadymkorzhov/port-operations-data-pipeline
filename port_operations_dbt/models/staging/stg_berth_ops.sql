SELECT  operation_id,
        vessel_call_id,
        berth_id,
        operation_type,
        planned_start,
        actual_start,
        planned_end,
        actual_end,
        UPPER(TRIM(status)) AS status,
        updated_at
FROM {{source('port_ops','berth_ops_raw')}}