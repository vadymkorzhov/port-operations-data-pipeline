SELECT *
FROM {{ ref('stg_berth_ops') }}
WHERE actual_start > actual_end