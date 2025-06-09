import pandas as pd
import boto3
import io
from config import AWS_BUCKET, RAW_KEY, LOCAL_FILE

def load_raw_data():
    try:
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=AWS_BUCKET, Key=RAW_KEY)
        df = pd.read_csv(io.BytesIO(obj['Body'].read()))
        print("✅ Loaded raw data from S3")
    except Exception as e:
        print(f"⚠️ Failed to load from S3. Using local file: {e}")
        df = pd.read_csv(LOCAL_FILE)
    return df
