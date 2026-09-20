from pathlib import Path
import csv
from datetime import datetime


OUTPUT_DIR = Path(__file__).resolve().parents[2] / "data" / "incoming"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


MOVEMENTS = [
    ["M10001", "MSCU1234567", "VC10001", "DISCHARGE", "2026-09-18 06:35:00", "QC01", 40, 26750],
    ["M10002", "CMAU7654321", "VC10001", "DISCHARGE", "2026-09-18 06:41:00", "QC01", 20, 18400],
    ["M10003", "MAEU9876543", "VC10001", "discharge", "2026-09-18 06:48:00", "QC02", 40, 29100],

    ["M10004", "TGHU4567890", "VC10002", "LOAD", "2026-09-18 08:05:00", "QC03", 40, 22400],
    ["M10005", "HLXU3456789", "VC10002", "LOAD", "2026-09-18 08:12:00", "QC03", 20, 15700],
    ["M10006", "OOLU2345678", "VC10002", "LOAD ", "2026-09-18 08:19:00", "QC04", 40, 24600],

    ["M10007", "MSCU8765432", "VC10003", "DISCHARGE", "2026-09-18 09:25:00", "QC02", 40, 27800],
    ["M10008", "CMAU1122334", "VC10003", "DISCHARGE", "2026-09-18 09:31:00", "QC02", 20, 16900],

    ["M10009", "MAEU5566778", "VC10004", "LOAD", "2026-09-18 11:22:00", "QC05", 40, 21500],
    ["M10010", "TGHU9988776", "VC10004", "LOAD", "2026-09-18 11:29:00", "QC05", 40, 25300],

    ["M10011", "HLXU4433221", "VC10005", "DISCHARGE", "2026-09-17 18:30:00", "QC01", 20, 14300],
    ["M10012", "OOLU6677889", "VC10005", "DISCHARGE", "2026-09-17 18:38:00", "QC01", 40, 28400],

    ["M10013", "MSCU1357924", "VC10006", "LOAD", "2026-09-17 20:31:00", "QC04", 40, 23800],
    ["M10014", "CMAU2468135", "VC10006", "LOAD", "2026-09-17 20:39:00", None, 20, 12600],

    ["M10015", "MAEU1928374", "VC10007", "DISCHARGE", "2026-09-18 13:21:00", "QC03", 40, 27200],
    ["M10016", "TGHU9182736", "VC10007", "DISCHARGE", "2026-09-18 13:28:00", "QC03", 20, 15100],

    ["M10017", "HLXU5647382", "VC10008", "LOAD", "2026-09-18 15:17:00", "QC02", 40, 22900],
    ["M10018", "OOLU1029384", "VC10008", "LOAD", "2026-09-18 15:24:00", "QC02", 40, 26100],
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