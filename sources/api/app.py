from fastapi import FastAPI

app = FastAPI(
    title="Port Vessel Calls API",
    version="1.0"
)


VESSEL_CALLS = [
    {
        "vessel_call_id": "VC10001",
        "imo": "9780471",
        "vessel_name": "Baltic Horizon",
        "service": "NEU1",
        "terminal": "CT1",
        "berth": "B01",
        "eta": "2026-09-18T05:30:00Z",
        "etd": "2026-09-18T12:30:00Z",
        "status": "IN_PORT",
        "updated_at": "2026-09-18T06:18:00Z"
    },
    {
        "vessel_call_id": "VC10002",
        "imo": "9812345",
        "vessel_name": "Atlantic Trader",
        "service": "MED2",
        "terminal": "CT1",
        "berth": "B03",
        "eta": "2026-09-18T07:00:00Z",
        "etd": "2026-09-18T15:00:00Z",
        "status": "IN_PORT",
        "updated_at": "2026-09-18T07:42:00Z"
    },
    {
        "vessel_call_id": "VC10003",
        "imo": "9734567",
        "vessel_name": "Nordic Star",
        "service": "BSEA1",
        "terminal": "CT1",
        "berth": "B02",
        "eta": "2026-09-18T08:30:00Z",
        "etd": "2026-09-18T16:30:00Z",
        "status": "EXPECTED",
        "updated_at": "2026-09-18T05:20:00Z"
    },
    {
        "vessel_call_id": "VC10004",
        "imo": "9687654",
        "vessel_name": "Danube Express",
        "service": "MED1",
        "terminal": "CT2",
        "berth": "B04",
        "eta": "2026-09-18T10:30:00Z",
        "etd": "2026-09-18T18:30:00Z",
        "status": "EXPECTED",
        "updated_at": "2026-09-18T05:45:00Z"
    },
    {
        "vessel_call_id": "VC10005",
        "imo": "9567890",
        "vessel_name": "Ocean Pioneer",
        "service": "NEU2",
        "terminal": "CT1",
        "berth": "B01",
        "eta": "2026-09-17T17:30:00Z",
        "etd": "2026-09-18T01:30:00Z",
        "status": "DEPARTED",
        "updated_at": "2026-09-18T01:24:00Z"
    },
    {
        "vessel_call_id": "VC10006",
        "imo": "9456789",
        "vessel_name": "Mediterranean Sun",
        "service": "MED3",
        "terminal": "CT2",
        "berth": "B05",
        "eta": "2026-09-17T19:30:00Z",
        "etd": "2026-09-18T03:00:00Z",
        "status": "departed",
        "updated_at": "2026-09-18T02:51:00Z"
    },
    {
        "vessel_call_id": "VC10007",
        "imo": "9345678",
        "vessel_name": "Black Sea Voyager",
        "service": "BSEA2",
        "terminal": "CT1",
        "berth": "B03",
        "eta": "2026-09-18T12:30:00Z",
        "etd": "2026-09-18T20:30:00Z",
        "status": "EXPECTED",
        "updated_at": "2026-09-18T06:10:00Z"
    },
    {
        "vessel_call_id": "VC10008",
        "imo": "9234567",
        "vessel_name": "Adriatic Pearl",
        "service": "MED4",
        "terminal": "CT2",
        "berth": "B02",
        "eta": "2026-09-18T14:30:00Z",
        "etd": "2026-09-18T22:30:00Z",
        "status": "EXPECTED ",
        "updated_at": "2026-09-18T06:30:00Z"
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