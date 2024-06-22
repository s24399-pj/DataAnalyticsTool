import pandas as pd
import os.path
from pathlib import Path

def load_data(file_path: str, separator: str) -> pd.DataFrame:
    current_dir = Path(__file__).parent.parent.parent
    current_dir = os.path.join(current_dir, "data")
    dataset_path = os.path.join(current_dir, file_path)
    try:
        raw_df = pd.read_csv(dataset_path, sep=separator, header=0)
        return raw_df
    except Exception as e:
        raise Exception(f"Exception while loading data: {e}")