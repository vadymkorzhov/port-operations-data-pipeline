from sqlalchemy import create_engine,text
from pathlib import Path
from dotenv import load_dotenv
import os
import pandas as pd

base_dir = Path(__file__).resolve().parent
load_dotenv(base_dir.parent / ".env")

host = os.getenv("PORT_OPS_HOST")
port = os.getenv("PORT_OPS_PORT")
db = os.getenv("PORT_OPS_DB")
user =os.getenv("PORT_OPS_USER")
password = os.getenv("PORT_OPS_PASSWORD")
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")

def create_raw_schema_and_tables():
    query = text("""
    CREATE SCHEMA IF NOT EXISTS raw;

    CREATE TABLE IF NOT EXISTS raw.vessel_raw (
        vessel_call_id VARCHAR,
        imo NUMERIC,
        vessel_name TEXT,
        service VARCHAR,
        terminal VARCHAR,
        berth VARCHAR,
        eta TIMESTAMP,
        etd TIMESTAMP,
        status TEXT,
        updated_at TIMESTAMP,
        UNIQUE (vessel_call_id)
    );

    CREATE TABLE IF NOT EXISTS raw.cargo_ops_raw (
        move_id VARCHAR,
        container_id VARCHAR,
        vessel_call_id VARCHAR,
        move_type TEXT,
        event_time TIMESTAMP,
        crane_id VARCHAR,
        container_size VARCHAR,
        weight_kg NUMERIC,
        UNIQUE (move_id)
    );

    CREATE TABLE IF NOT EXISTS raw.berth_ops_raw (
        operation_id VARCHAR,
        vessel_call_id VARCHAR,
        berth_id VARCHAR,
        operation_type VARCHAR,
        planned_start TIMESTAMP,
        actual_start TIMESTAMP,
        planned_end TIMESTAMP,
        actual_end TIMESTAMP,
        status VARCHAR,
        updated_at TIMESTAMP,
        UNIQUE (operation_id)
    );
    """)

    with engine.begin() as conn:
        conn.execute(query)


def load_vessel_data(vessel_df):
    records = vessel_df.to_dict(orient="records")
    query = text("""
    INSERT INTO raw.vessel_raw (
        vessel_call_id,
        imo,
        vessel_name,
        service,
        terminal,
        berth,
        eta,
        etd,
        status,
        updated_at) 
        VALUES (
        :vessel_call_id,
        :imo,
        :vessel_name,
        :service,
        :terminal,
        :berth,
        :eta,
        :etd,
        :status,
        :updated_at)
        ON CONFLICT (vessel_call_id) DO UPDATE SET
        imo = EXCLUDED.imo,
        vessel_name = EXCLUDED.vessel_name,
        service = EXCLUDED.service,
        terminal = EXCLUDED.terminal,
        berth = EXCLUDED.berth,
        eta = EXCLUDED.eta,
        etd = EXCLUDED.etd,
        status = EXCLUDED.status,
        updated_at = EXCLUDED.updated_at
        WHERE EXCLUDED.updated_at > raw.vessel_raw.updated_at; """)
    with engine.begin() as conn:
        conn.execute(query, records)

def load_cargo_data(cargo_ops_df):
    records = cargo_ops_df.to_dict(orient="records")
    query = text("""
        INSERT INTO raw.cargo_ops_raw (
        move_id,
        container_id,
        vessel_call_id,
        move_type,
        event_time,
        crane_id,
        container_size,
        weight_kg)
        VALUES (
        :move_id,
        :container_id,
        :vessel_call_id,
        :move_type,
        :event_time,
        :crane_id,
        :container_size,
        :weight_kg)
        ON CONFLICT (move_id) DO NOTHING;
        """)
    with engine.begin() as conn:
        conn.execute(query, records)

def load_berth_ops_data(berth_ops_df):
    berth_ops_df = berth_ops_df.astype(object).where(pd.notnull(berth_ops_df), None)
    records = berth_ops_df.to_dict(orient="records")
    query = text("""
        INSERT INTO raw.berth_ops_raw (
        operation_id,
        vessel_call_id,
        berth_id,
        operation_type,
        planned_start,
        actual_start,
        planned_end,
        actual_end,
        status,
        updated_at)
        VALUES (
        :operation_id,
        :vessel_call_id,
        :berth_id,
        :operation_type,
        :planned_start,
        :actual_start,
        :planned_end,
        :actual_end,
        :status,
        :updated_at)
        ON CONFLICT (operation_id) DO UPDATE SET
        vessel_call_id = EXCLUDED.vessel_call_id,
        berth_id = EXCLUDED.berth_id,
        operation_type = EXCLUDED.operation_type,
        planned_start = EXCLUDED.planned_start,
        actual_start = EXCLUDED.actual_start,
        planned_end = EXCLUDED.planned_end,
        actual_end = EXCLUDED.actual_end,
        status = EXCLUDED.status,
        updated_at = EXCLUDED.updated_at
        WHERE EXCLUDED.updated_at > raw.berth_ops_raw.updated_at;     
    
    """)
    with engine.begin() as conn:
        conn.execute(query, records)