import pandas as pd

class Dataset:

    def __init__(self, raw_df: pd.DataFrame, name: str, filename: str):
        self._raw_df = raw_df
        self._name = name
        self._filename = filename
        self._processed_df = raw_df

    def get_raw_df(self):
        return self._raw_df

    def get_name(self):
        return self._name

    def get_filename(self):
        return self._filename

    def get_processed_df(self):
        return self._processed_df

    def set_processed_df(self, input_df: pd.DataFrame):
        self._processed_df = input_df
