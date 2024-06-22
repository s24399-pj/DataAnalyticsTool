import pandas as pd


def describe_dataset(dataframe: pd.DataFrame, id_column: str):
    pd.set_option('display.max_columns', None)
    print("___________________________")

    print("Dataset head():")
    print(dataframe.head())

    print("___________________________")

    print(print("\nDataset dimensions: " + str(dataframe.shape) + "\n"))

    print("___________________________")

    print(f"Null values count in dataset:\n {dataframe.isnull().sum()}")
    print(f"Perc null values in dataset:\n {dataframe.isnull().sum() / len(dataframe) * 100}")

    print("___________________________")

    print("Dataset datatypes:")
    print(dataframe.info())
    print("Detailed dataset datatypes:")
    for column in dataframe.columns:
        print(f"Data types in column {column} column: {dataframe[column].apply(lambda x: type(x).__name__).unique()}")

    print("___________________________")

    print(f"Does column {id_column} contain duplicates? : " + str(not dataframe[id_column].is_unique))

    print("___________________________")

    unique_values_perc_dict = dict()
    for column_name in dataframe:
        unique_values_perc_dict[
            column_name] = dataframe[column_name].nunique() / len(dataframe[column_name]) * 100
    print("Unique values percentage in columns:")
    for key, value in unique_values_perc_dict.items():
        print(f"{key} : {round(value, 1)} %")

    print("___________________________")

    print("Basic statistics of dataset")
    print(dataframe.describe())


    print("___________________________")

