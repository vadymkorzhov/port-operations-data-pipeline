SELECT operation_id,status,actual_start,actual_end
FROM {{ ref('stg_berth_ops') }}
WHERE status = 'IN_PROGRESS' AND actual_start IS NULL