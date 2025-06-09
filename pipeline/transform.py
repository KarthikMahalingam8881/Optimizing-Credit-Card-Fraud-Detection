import pandas as pd

# Feature engineering from your Colab notebook (simplified)
def transform_data(df):
    df = df = df.drop_duplicates().copy()
    df['Amount_V20_Interaction'] = df['Amount'] * df['V20']
    df['V17_V12_Interaction'] = df['V17'] * df['V12']
    df['Fraudulent_Outlier_Flag'] = ((df['Amount'] > df['Amount'].quantile(0.99)) & (df['Class'] == 1)).astype(int)
    df['Amount_V_Interaction'] = df['Amount'] * df['V10']*df['V1']* df['V3']
    df['V17_V16_Interaction'] = df['V17'] * df['V16']
    df['High_V3_Flag'] = (df['V3'] > df['V3'].quantile(0.95)).astype(int)
    df['Low_V20_Flag'] = (df['V20'] < df['V20'].quantile(0.05)).astype(int)
    df['Amount_Time_V14'] = df['Amount'] * df['Time'] * df['V14']
    df['Z_Amount'] = (df['Amount'] - df['Amount'].mean()) / df['Amount'].std()
    df['Rolling_Mean_Amount'] = df['Amount'].rolling(window=10).mean().fillna(df['Amount'].mean())
    return df
