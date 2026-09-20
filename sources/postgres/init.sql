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


INSERT INTO berth_operations (
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
    'OP10001',
    'VC10001',
    'B01',
    'DISCHARGE',
    '2026-09-18 06:00:00',
    '2026-09-18 06:18:00',
    '2026-09-18 12:00:00',
    NULL,
    'IN_PROGRESS',
    '2026-09-18 06:18:00'
),

(
    'OP10002',
    'VC10002',
    'B03',
    'LOAD',
    '2026-09-18 07:30:00',
    '2026-09-18 07:42:00',
    '2026-09-18 14:30:00',
    NULL,
    'IN_PROGRESS',
    '2026-09-18 07:42:00'
),

(
    'OP10003',
    'VC10003',
    'B02',
    'DISCHARGE',
    '2026-09-18 09:00:00',
    NULL,
    '2026-09-18 16:00:00',
    NULL,
    'PLANNED',
    '2026-09-18 05:20:00'
),

(
    'OP10004',
    'VC10004',
    'B04',
    'LOAD',
    '2026-09-18 11:00:00',
    NULL,
    '2026-09-18 18:00:00',
    NULL,
    'PLANNED',
    '2026-09-18 05:45:00'
),

(
    'OP10005',
    'VC10005',
    'B01',
    'DISCHARGE',
    '2026-09-17 18:00:00',
    '2026-09-17 18:11:00',
    '2026-09-18 01:00:00',
    '2026-09-18 01:24:00',
    'COMPLETED',
    '2026-09-18 01:24:00'
),

(
    'OP10006',
    'VC10006',
    'B05',
    'LOAD',
    '2026-09-17 20:00:00',
    '2026-09-17 20:05:00',
    '2026-09-18 03:00:00',
    '2026-09-18 02:51:00',
    'completed',
    '2026-09-18 02:51:00'
),

(
    'OP10007',
    'VC10007',
    'B03',
    'DISCHARGE',
    '2026-09-18 13:00:00',
    NULL,
    '2026-09-18 20:00:00',
    NULL,
    'SCHEDULED',
    '2026-09-18 06:10:00'
),

(
    'OP10008',
    'VC10008',
    'B02',
    'LOAD',
    '2026-09-18 15:00:00',
    NULL,
    '2026-09-18 22:00:00',
    NULL,
    'PLANNED ',
    '2026-09-18 06:30:00'
);