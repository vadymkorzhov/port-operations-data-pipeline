CREATE TABLE berth_operations (
    operation_id VARCHAR(20) PRIMARY KEY,
    vessel_call_id VARCHAR(20) NOT NULL,
    berth_id VARCHAR(10) NOT NULL,
    operation_type VARCHAR(30) NOT NULL,

    planned_start TIMESTAMP NOT NULL,
    actual_start TIMESTAMP,

    planned_end TIMESTAMP NOT NULL,
    actual_end TIMESTAMP,

    status VARCHAR(30) NOT NULL,

    updated_at TIMESTAMP NOT NULL
);


INSERT INTO public.berth_operations (
    operation_id,
    vessel_call_id,
    berth_id,
    operation_type,
    planned_start,
    actual_start,
    planned_end,
    actual_end,
    status,
    updated_at
)
VALUES
(
    'OP10001', 'VC10001', 'B01', 'DISCHARGE',
    '2026-09-18 06:30:00',
    '2026-09-18 06:45:00',
    '2026-09-18 12:00:00',
    '2026-09-18 12:20:00',
    'COMPLETED',
    '2026-09-18 12:30:00'
),
(
    'OP10002', 'VC10002', 'B02', 'LOAD',
    '2026-09-18 08:30:00',
    '2026-09-18 08:40:00',
    '2026-09-18 18:00:00',
    '2026-09-18 18:35:00',
    'completed',
    '2026-09-18 18:45:00'
),
(
    'OP10003', 'VC10003', 'B03', 'DISCHARGE',
    '2026-09-19 05:30:00',
    '2026-09-19 05:25:00',
    '2026-09-19 14:00:00',
    '2026-09-19 13:40:00',
    'COMPLETED',
    '2026-09-19 14:00:00'
),
(
    'OP10004', 'VC10004', 'B01', 'DISCHARGE',
    '2026-09-20 07:30:00',
    '2026-09-20 07:45:00',
    '2026-09-20 16:00:00',
    NULL,
    'IN_PROGRESS',
    '2026-09-20 14:00:00'
),
(
    'OP10005', 'VC10005', 'B04', 'LOAD',
    '2026-09-20 10:30:00',
    '2026-09-20 10:50:00',
    '2026-09-20 20:00:00',
    NULL,
    'IN_PROGRESS',
    '2026-09-20 16:00:00'
),
(
    'OP10006', 'VC10006', 'B02', 'DISCHARGE',
    '2026-09-22 06:30:00',
    NULL,
    '2026-09-22 14:00:00',
    NULL,
    'PLANNED ',
    '2026-09-21 12:00:00'
),
(
    'OP10007', 'VC10007', 'B03', 'LOAD',
    '2026-09-22 14:30:00',
    NULL,
    '2026-09-22 23:00:00',
    NULL,
    'PLANNED',
    '2026-09-21 12:30:00'
),
(
    'OP10008', 'VC10008', 'B01', 'DISCHARGE',
    '2026-09-23 04:30:00',
    NULL,
    '2026-09-23 14:00:00',
    NULL,
    'PLANNED',
    '2026-09-21 13:00:00'
);