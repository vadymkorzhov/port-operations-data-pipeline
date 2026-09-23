SELECT operation_id,status,actual_start,actual_end
FROM {{ ref('stg_berth_ops') }}
WHERE status = 'COMPLETED' AND (actual_start IS NULL OR actual_end IS NULL)