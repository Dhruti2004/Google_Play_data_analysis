# Data Cleaning Script for Google Play Store Dataset
import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.drop_duplicates()
    df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True)
    df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
    df['Price'] = df['Price'].str.replace('$', '', regex=True)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df = df.dropna(subset=['Rating'])
    df.to_csv(output_path, index=False)
