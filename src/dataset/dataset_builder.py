import pandas as pd

from src.dataset.dataset import Dataset

class DatasetBuilder:
    def __init__(self):
        self._raw_df = None
        self._name = None
        self._filename = None

    def set_raw_df(self, raw_df: pd.DataFrame):
        self._raw_df = raw_df
        return self

    def set_name(self, name: str):
        self._name = name
        return self

    def set_filename(self, filename: str):
        self._filename = filename
        return self

    def build(self):
        if self._raw_df is None or self._name is None or self._filename is None:
            raise ValueError("Missing required attributes to build Dataset object.")
        return Dataset(self._raw_df, self._name, self._filename)
