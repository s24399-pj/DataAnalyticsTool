from typing import Tuple

import pandas as pd

def drop_and_count_duplicate_rows(input_df: pd.DataFrame) -> Tuple[pd.DataFrame, int]:
    processed_df = input_df.copy()
    processed_df.drop_duplicates(inplace=True)
    duplicates_count = len(input_df) - len(processed_df)
    return processed_df, duplicates_count

def drop_and_count_NA_values(input_df: pd.DataFrame) -> Tuple[pd.DataFrame, int]:
    processed_df = input_df.copy()
    processed_df.dropna(inplace=True)
    na_count = len(input_df) - len(processed_df)
    return processed_df, na_count

def date_columns_to_datetime(input_df: pd.DataFrame) -> pd.DataFrame:
    processed_df = input_df.copy()
    for column in processed_df.columns:
        if "date" in str(column).lower():
            processed_df[column] = pd.to_datetime(processed_df[column], format='%Y-%m-%d')
    return processed_df



#Transaction ID,Date,Product Category,Product Name,Units Sold,Unit Price,Total Revenue,Region,Payment Method