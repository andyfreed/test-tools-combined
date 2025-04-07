import pandas as pd
from datetime import datetime
import numpy as np

def validate_columns(df, required_columns):
    """Validate if required columns exist in the dataframe"""
    missing_columns = [col for col in required_columns if col not in df.columns]
    return len(missing_columns) == 0, missing_columns

def clean_data(df):
    """Clean and prepare data"""
    # Create copy to avoid modifying original
    df_clean = df.copy()

    # Remove any trailing/leading whitespace
    for col in df_clean.columns:
        if df_clean[col].dtype == 'object':
            df_clean[col] = df_clean[col].str.strip()

    # Convert date format
    df_clean['Completed'] = pd.to_datetime(df_clean['Completed'])

    # Convert numeric columns and handle empty values
    df_clean['License number'] = pd.to_numeric(df_clean['License number'].replace('', np.nan), errors='coerce').astype('Int64')
    df_clean['CFP Board Course ID'] = pd.to_numeric(df_clean['CFP Board Course ID'], errors='coerce')

    return df_clean

def map_columns(df):
    """Map columns according to requirements"""
    mapping = {
        'CFP Board Course ID': 'CFP Program ID',
        'Completed': 'Date Individual Completed',
        'License number': 'Attendee CFP Board ID',
        'Last name': 'attendee last name',
        'First name': 'attendee first name'
    }

    # Select and rename columns
    df_mapped = df[list(mapping.keys())].copy()
    df_mapped = df_mapped.rename(columns=mapping)

    # Format date column as short date
    df_mapped['Date Individual Completed'] = df_mapped['Date Individual Completed'].dt.strftime('%m/%d/%Y')

    #Format numeric columns to remove commas
    df_mapped['CFP Program ID'] = df_mapped['CFP Program ID'].astype(str).str.replace(',', '', regex=False)
    df_mapped['Attendee CFP Board ID'] = df_mapped['Attendee CFP Board ID'].astype(str).str.replace('.0', '', regex=False).str.replace(',', '', regex=False)

    # Add empty Attendee Middle Name column at the end
    df_mapped['Attendee Middle Name'] = ''

    return df_mapped

def process_file(input_df):
    """Process the input dataframe and return mapped dataframe"""
    required_columns = [
        'CFP Board Course ID',
        'Completed',
        'License number',
        'Last name',
        'First name'
    ]

    # Validate columns
    columns_valid, missing_columns = validate_columns(input_df, required_columns)
    if not columns_valid:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    # Clean data
    df_clean = clean_data(input_df)

    # Map columns
    df_mapped = map_columns(df_clean)

    return df_mapped