from extract import load_raw_data
from transform import transform_data
from load import load_to_postgres

def run_pipeline():
    df_raw = load_raw_data()
    df_cleaned = transform_data(df_raw)
    load_to_postgres(df_cleaned)

if __name__ == '__main__':
    run_pipeline()
