import pandas as pd
from datetime import datetime
import json
from io import BytesIO

def save_to_s3(data,s3,s3_bucket,s3_key):
    s3.put_object(Body = data,Bucket =s3_bucket,Key =s3_key)

def build_s3_key(name, extension):
    now = datetime.now()

    timestamp = now.strftime("%Y%m%d_%H%M%S_%f")
    date_path = now.strftime("%Y/%m/%d")

    return f"raw/{name}/{date_path}/{name}_{timestamp}.{extension}"


def read_from_s3(s3, s3_bucket, key):
    response = s3.get_object(
        Bucket=s3_bucket,
        Key=key
    )
    return response["Body"]


def read_json(s3, s3_bucket, key):
    file_content = read_from_s3(s3, s3_bucket, key)
    data = json.loads(file_content.read().decode("utf-8"))
    return pd.DataFrame(data["data"])


def read_csv(s3, s3_bucket, key):
    file_content = read_from_s3(s3, s3_bucket, key)
    return pd.read_csv(file_content)


def read_parquet(s3, s3_bucket, key):
    file_content = read_from_s3(s3, s3_bucket, key)
    data = file_content.read()
    return pd.read_parquet(BytesIO(data))