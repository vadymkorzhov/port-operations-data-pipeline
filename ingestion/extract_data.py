import json
import shutil

import requests
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os
from s3 import build_s3_key,save_to_s3

base_dir = Path(__file__).resolve().parent
load_dotenv(base_dir.parent / ".env")

source_user = os.getenv("POSTGRES_USER")
source_password = os.getenv("POSTGRES_PASSWORD")
source_host = os.getenv("POSTGRES_HOST")
source_port = os.getenv("POSTGRES_PORT")
source_db = os.getenv("POSTGRES_DB")

def extract_api_data(url,s3,s3_bucket):
    response = requests.get(url,timeout=30)
    response.raise_for_status()
    api_data = response.json()
    data = json.dumps(api_data).encode("utf8")

    s3_key = build_s3_key("vessel_calls","json")
    save_to_s3(data,s3,s3_bucket,s3_key)
    return s3_key

def extract_csv_data(incoming_folder,s3,s3_bucket):
    extracted_files= []

    for csv_path in incoming_folder.glob("*.csv"):
        with open(csv_path, "rb") as f:
            csv_data = f.read()
        s3_key =build_s3_key("cargo_operations","csv")
        extracted_files.append({
            "s3_key": s3_key,
            "csv_path": csv_path,
        })
        save_to_s3(csv_data,s3,s3_bucket,s3_key)

    return extracted_files


def extract_postgres_data(s3,s3_bucket):
    engine = create_engine(
        f"postgresql+psycopg2://{source_user}:{source_password}@{source_host}:{source_port}/{source_db}")
    query = text('''SELECT * FROM public.berth_operations''')
    postgres_raw_df = pd.read_sql(query, engine)
    berth_ops = postgres_raw_df.to_parquet(index=False)

    s3_key = build_s3_key("berth_operations","parquet")
    save_to_s3(berth_ops,s3,s3_bucket,s3_key)
    engine.dispose()
    return s3_key













