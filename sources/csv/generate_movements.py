from pathlib import Path
import csv
from datetime import datetime


OUTPUT_DIR = Path(__file__).resolve().parents[2] / "data" / "incoming"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


MOVEMENTS = [
    ["M10001", "CONT001", "VC10001", "DISCHARGE", "2026-09-18 07:00:00", "QC01", "40", 28400],
    ["M10002", "CONT002", "VC10001", "DISCHARGE", "2026-09-18 08:15:00", "QC01", "20", 17200],
    ["M10003", "CONT003", "VC10001", "DISCHARGE", "2026-09-18 10:30:00", "QC02", "40", 30100],
    ["M10004", "CONT004", "VC10001", "DISCHARGE", "2026-09-18 11:45:00", None,   "20", 15600],

    ["M10005", "CONT005", "VC10002", "LOAD", "2026-09-18 09:15:00", "QC03", "40", 26300],
    ["M10006", "CONT006", "VC10002", "load", "2026-09-18 11:30:00", "QC03", "20", 14800],
    ["M10007", "CONT007", "VC10002", "LOAD ", "2026-09-18 14:00:00", "QC04", "40", 29100],
    ["M10008", "CONT008", "VC10002", "LOAD", "2026-09-18 17:20:00", "QC04", "20", 16500],

    ["M10009", "CONT009", "VC10003", "DISCHARGE", "2026-09-19 06:15:00", "QC01", "40", 27800],
    ["M10010", "CONT010", "VC10003", "discharge", "2026-09-19 08:30:00", "QC02", "40", 31200],
    ["M10011", "CONT011", "VC10003", "DISCHARGE", "2026-09-19 11:00:00", "QC01", "20", 13900],
    ["M10012", "CONT012", "VC10003", "DISCHARGE", "2026-09-19 13:10:00", "QC02", "20", 18100],

    ["M10013", "CONT013", "VC10004", "DISCHARGE", "2026-09-20 08:30:00", "QC01", "40", 29500],
    ["M10014", "CONT014", "VC10004", "DISCHARGE", "2026-09-20 10:45:00", "QC01", "20", 15100],
    ["M10015", "CONT015", "VC10004", "DISCHARGE", "2026-09-20 13:15:00", "QC02", "40", 32400],

    ["M10016", "CONT016", "VC10005", "LOAD", "2026-09-20 11:30:00", "QC03", "20", 14300],
    ["M10017", "CONT017", "VC10005", "LOAD", "2026-09-20 13:45:00", "QC03", "40", 28700],
    ["M10018", "CONT018", "VC10005", "LOAD", "2026-09-20 15:30:00", "QC04", "40", 30600]
]


HEADERS = [
    "move_id",
    "container_id",
    "vessel_call_id",
    "move_type",
    "event_time",
    "crane_id",
    "container_size",
    "weight_kg",
]


def generate_csv():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file = OUTPUT_DIR / f"container_movements_{timestamp}.csv"

    with output_file.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(HEADERS)
        writer.writerows(MOVEMENTS)

    print(f"Created: {output_file}")


if __name__ == "__main__":
    generate_csv()