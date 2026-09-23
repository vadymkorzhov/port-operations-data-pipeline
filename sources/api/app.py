from fastapi import FastAPI

app = FastAPI(
    title="Port Vessel Calls API",
    version="1.0"
)


VESSEL_CALLS  = [
    {
        "vessel_call_id": "VC10001",
        "imo": 9300001,
        "vessel_name": "Baltic Star",
        "service": "NE1",
        "terminal": "T1",
        "berth": "B01",
        "eta": "2026-09-18T06:00:00",
        "etd": "2026-09-18T18:00:00",
        "status": "DEPARTED",
        "updated_at": "2026-09-18T18:30:00"
    },
    {
        "vessel_call_id": "VC10002",
        "imo": 9300002,
        "vessel_name": "Ocean Blue",
        "service": "MED1",
        "terminal": "T1",
        "berth": "B02",
        "eta": "2026-09-18T08:00:00",
        "etd": "2026-09-18T22:00:00",
        "status": "departed",
        "updated_at": "2026-09-18T22:20:00"
    },
    {
        "vessel_call_id": "VC10003",
        "imo": 9300003,
        "vessel_name": "Northern Wind",
        "service": "NE2",
        "terminal": "T2",
        "berth": "B03",
        "eta": "2026-09-19T05:00:00",
        "etd": "2026-09-19T17:00:00",
        "status": "DEPARTED",
        "updated_at": "2026-09-19T17:15:00"
    },
    {
        "vessel_call_id": "VC10004",
        "imo": 9300004,
        "vessel_name": "Adriatic Pearl",
        "service": "MED2",
        "terminal": "T1",
        "berth": "B01",
        "eta": "2026-09-20T07:00:00",
        "etd": "2026-09-20T21:00:00",
        "status": "IN_PORT",
        "updated_at": "2026-09-20T14:00:00"
    },
    {
        "vessel_call_id": "VC10005",
        "imo": 9300005,
        "vessel_name": "Black Sea Trader",
        "service": "BS1",
        "terminal": "T2",
        "berth": "B04",
        "eta": "2026-09-20T10:00:00",
        "etd": "2026-09-21T02:00:00",
        "status": "IN_PORT",
        "updated_at": "2026-09-20T16:00:00"
    },
    {
        "vessel_call_id": "VC10006",
        "imo": 9300006,
        "vessel_name": "Danube Express",
        "service": "BS2",
        "terminal": "T1",
        "berth": "B02",
        "eta": "2026-09-22T06:00:00",
        "etd": "2026-09-22T18:00:00",
        "status": "EXPECTED ",
        "updated_at": "2026-09-21T12:00:00"
    },
    {
        "vessel_call_id": "VC10007",
        "imo": 9300007,
        "vessel_name": "Mediterranean Sky",
        "service": "MED1",
        "terminal": "T2",
        "berth": "B03",
        "eta": "2026-09-22T14:00:00",
        "etd": "2026-09-23T04:00:00",
        "status": "EXPECTED",
        "updated_at": "2026-09-21T12:30:00"
    },
    {
        "vessel_call_id": "VC10008",
        "imo": 9300008,
        "vessel_name": "Atlantic Horizon",
        "service": "NE1",
        "terminal": "T1",
        "berth": "B01",
        "eta": "2026-09-23T04:00:00",
        "etd": "2026-09-23T20:00:00",
        "status": "EXPECTED",
        "updated_at": "2026-09-21T13:00:00"
    }
]


@app.get("/api/v1/vessel-calls")
def get_vessel_calls():
    return {
        "count": len(VESSEL_CALLS),
        "data": VESSEL_CALLS
    }


@app.get("/health")
def health():
    return {"status": "ok"}