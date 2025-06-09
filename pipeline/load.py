import pandas as pd
from sqlalchemy import create_engine
from config import SQLALCHEMY_URI, POSTGRES_TABLE

def load_to_postgres(df):
    engine = create_engine(SQLALCHEMY_URI)
    df.to_sql(POSTGRES_TABLE, engine, if_exists='replace', index=False)
    print("✅ Loaded cleaned data into PostgreSQL")