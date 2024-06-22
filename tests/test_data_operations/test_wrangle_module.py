import unittest
import pandas as pd

from src.data_operations import wrangle_module

class TestWrangleModule(unittest.TestCase):

    def setUp(self):

        self.df_duplicates = pd.DataFrame({
            'A': [1, 2, 2, 4, 5, 6, 6],
            'B': ['a', 'b', 'b', 'd', 'e', 'f', 'f']
        })
        self.df_na = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': ['a', None, 'c', 'd', 'e']
        })
        self.df_dates = pd.DataFrame({
            'date': ['2023-01-01', '2023-02-01', '2023-03-01'],
            'value': [10, 20, 30]
        })

    def test_drop_and_count_duplicate_rows(self):
        processed_df, duplicates_count = wrangle_module.drop_and_count_duplicate_rows(self.df_duplicates)

        expected_df = pd.DataFrame({
            'A': [1, 2, 4, 5, 6],
            'B': ['a', 'b', 'd', 'e', 'f']
        })

        pd.testing.assert_frame_equal(processed_df.reset_index(drop=True), expected_df)

        self.assertEqual(duplicates_count, 2)

    def test_drop_and_count_NA_values(self):
        processed_df, na_count = wrangle_module.drop_and_count_NA_values(self.df_na)

        expected_df = pd.DataFrame({
            'A': [1.0, 4.0, 5.0],
            'B': ['a', 'd', 'e']
        })

        pd.testing.assert_frame_equal(processed_df.reset_index(drop=True), expected_df)

        self.assertEqual(na_count, 2)

    def test_date_columns_to_datetime(self):
        processed_df = wrangle_module.date_columns_to_datetime(self.df_dates)

        expected_df = pd.DataFrame({
            'date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01']),
            'value': [10, 20, 30]
        })

        pd.testing.assert_frame_equal(processed_df, expected_df)


if __name__ == '__main__':
    unittest.main()
