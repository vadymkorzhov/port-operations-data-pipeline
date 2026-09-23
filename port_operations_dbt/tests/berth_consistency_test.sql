SELECT
    v.vessel_call_id,
    v.berth,
    b.berth_id
FROM {{ ref('stg_vessel') }} v
JOIN {{ ref('stg_berth_ops') }} b
    ON v.vessel_call_id = b.vessel_call_id
WHERE v.berth <> b.berth_id