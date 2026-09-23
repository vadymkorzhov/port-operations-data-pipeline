import json
import shutil
import boto3
from pathlib import Path
from extract_data import extract_api_data,extract_csv_data,extract_postgres_data
from s3 import read_json,read_csv,read_parquet
from load_data import create_raw_schema_and_tables,load_vessel_data,load_cargo_data,load_berth_ops_data
from dotenv import load_dotenv
import os

base_dir = Path(__file__).resolve().parent
load_dotenv(base_dir.parent / ".env")



def main():

    config_path = base_dir.parent / "config" / 'port_ops_config.json'
    incoming_folder = base_dir.parent / "data" / "incoming"
    processed_folder = base_dir.parent / "data" / "processed"

    with open(config_path) as f:
        config = json.load(f)

    url = os.getenv("VESSEL_API_URL")
    s3_bucket = config["s3_bucket"]
    s3 = boto3.client("s3")

    create_raw_schema_and_tables()
    vessel_key = extract_api_data(url,s3,s3_bucket)
    berth_ops_key = extract_postgres_data(s3,s3_bucket)
    vessel_calls_df = read_json(s3,s3_bucket,vessel_key)
    berth_ops_df = read_parquet(s3, s3_bucket, berth_ops_key)
    cargo_ops_extracted_files = extract_csv_data(incoming_folder,s3,s3_bucket)
    load_vessel_data(vessel_calls_df)
    load_berth_ops_data(berth_ops_df)
    for file_info in cargo_ops_extracted_files:
        key = file_info["s3_key"]
        csv_path = file_info["csv_path"]

        cargo_ops_df = read_csv(s3, s3_bucket, key)

        load_cargo_data(cargo_ops_df)  # must succeed first
        processed_folder.mkdir(parents=True, exist_ok=True)
        destination = processed_folder / csv_path.name
        shutil.move(csv_path, destination)


if __name__ == "__main__":
    main()