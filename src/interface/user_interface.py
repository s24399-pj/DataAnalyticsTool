from src.data_operations import operations_module
from src.data_operations import wrangle_module
from src.dataset.dataset import Dataset
from src.dataset.dataset_builder import DatasetBuilder
from src.data_analysing import analyse_module
from src.data_plotting import plot_module

DEFAULT_DATASET_FILEPATH = "Online Sales Data.csv"


class UserInterface:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.main()
        self.initialized = True

    def show_main_menu(self):
        print("___________________________")
        print("-- MAIN MENU --")
        print("1 - Load dataset")
        print("2 - Describe dataset")
        print("3 - Choose (change) loaded dataset")
        print("4 - Perform data wrangling operations")
        print("5 - Run exploratory data analysis")
        print("Q - Quit")
        print("\nChoose option number:")
        user_input = str(input()).upper()
        if user_input not in ["1", "2", "3", "4", "5", 'Q']:
            raise ValueError("Invalid option given.")
        return user_input

    def load_dataset(self):
        print("___________________________")
        print("Please input name of *.CSV dataset located in data folder:"
              "\n(Type 'default' to load \"Online Sales Data.csv\")")
        user_input = str(input())
        print("Please input separator used in the dataset:"
              "Default dataset: type ,")
        user_input2 = str(input())

        if user_input == "default":
            user_input = DEFAULT_DATASET_FILEPATH

        return operations_module.load_data(user_input, user_input2), user_input

    def choose_columns(self, df_columns: list, df_column_index_string: list, max_inputs: int, message: str):
        print("___________________________")
        print("Choose dataset columns.")
        print(message)
        for index, x in enumerate(df_columns):
            print(f"{index + 1} - {x}")
        user_input = str(input()).lower()
        if user_input.lower() == "default":
            return user_input
        elif "," in user_input and max_inputs > 1:
            user_input_index_list = user_input.split(",")
            if max_inputs != 999 and len(user_input_index_list) != max_inputs:
                raise ValueError("Too many arguments given.")
            user_input_column_list = list()
            for index in user_input_index_list:
                if index not in df_column_index_string:
                    raise ValueError("Invalid option given (column index).")
                user_input_column_list.append(df_columns[int(index) - 1])
            return user_input_column_list
        else:
            if user_input not in df_column_index_string:
                raise ValueError("Invalid option given (column index).")
            return user_input

    def describe_dataset(self, given_dataset: Dataset):
        dataframe_columns = list(given_dataset.get_processed_df().columns)
        column_index_strings = [str(i) for i in range(1, len(given_dataset.get_processed_df().columns) + 1)]
        message = "Choose one ID (key) column for dataset description:"
        user_input = self.choose_columns(dataframe_columns, column_index_strings, 1, message)
        chosen_id_column = given_dataset.get_processed_df().columns[int(user_input) - 1]
        analyse_module.describe_dataset(given_dataset.get_processed_df(), chosen_id_column)

    def choose_dataset(self):
        print("___________________________")
        print("Choose dataset: ")
        for index, x in enumerate(datasets):
            print(f"{index + 1} - {x.get_name()} : {x.get_filename()}")
        user_input = str(input())
        if user_input not in [str(i) for i in range(1, len(datasets) + 1)]:
            raise ValueError("Invalid option given.")
        dataset_index = int(user_input) - 1
        return datasets[dataset_index]

    def perform_data_wrangling(self, given_dataset: Dataset):
        processed_df, dup_rows_count = wrangle_module.drop_and_count_duplicate_rows(given_dataset.get_processed_df())
        processed_df, na_count = wrangle_module.drop_and_count_NA_values(processed_df)
        processed_df = wrangle_module.date_columns_to_datetime(processed_df)
        given_dataset.set_processed_df(processed_df)
        print("___________________________")
        print(f"Data wrangling performed.\n"
              f"- Dataset cleaned from duplicated rows and NA values.\n"
              f"- Date columns type changed to datetime\n"
              f"Duplicated rows count: {dup_rows_count}\n"
              f"NA values count: {na_count}")
        print("___________________________")

    def perform_exploratory_data_analysis(self, given_dataset: Dataset):

        # Transaction ID, Date, Product Category, Product Name, Units Sold, Unit Price, Total Revenue, Region,     Payment Method
        # 10001,     2024-01-01,Electronics,     iPhone 14 Pro,  2,          999.99,        1999.98,  North America,Credit Card

        dataframe_columns = list(given_dataset.get_processed_df().columns)
        column_index_strings = [str(i) for i in range(1, len(given_dataset.get_processed_df().columns) + 1)]

        # GENERAL HISTOGRAMS:
        message = ("Choose numeric columns for general histogram of dataset."
                   "\n(separate with comma - e.g.: 1,2,4)"
                   "\n[Type default for Units Sold, Unit Price, Total Revenue columns in default dataset]")
        chosen_histogram_columns = self.choose_columns(dataframe_columns, column_index_strings, 999, message)
        if chosen_histogram_columns == "default":
            chosen_histogram_columns = ["Units Sold", "Unit Price", "Total Revenue"]
        print("___________________________")
        print(f"Plotting general histogram for dataset {given_dataset.get_filename()}.")
        plot_module.show_histogram(given_dataset.get_processed_df(), chosen_histogram_columns)


        # DISTRIBUTION ON DATASET
        message = ("Choose columns for distribution analyse of dataset."
                   "\n(separate with comma - e.g.: 1,2,4)"
                   "\n[Type default for distribution of Product Category, Region, Payment Method - default dataset]")
        chosen_distribution_columns = self.choose_columns(dataframe_columns, column_index_strings, 999, message)
        if chosen_distribution_columns == "default":
            chosen_distribution_columns = ["Product Category", "Region", "Payment Method"]
        print("___________________________")
        print(f"Plotting analyse distribution on dataset {given_dataset.get_filename()}.")
        for column in chosen_distribution_columns:
            value_count = given_dataset.get_processed_df()[
                column].value_counts()
            plot_module.make_bar_plot_counts(value_count, ["orange"], f"Distribution of {column}", column, "Counts")

            value_count_percentage = given_dataset.get_processed_df()[column].value_counts(normalize=True) * 100
            plot_module.make_pie_chart_percent(value_count_percentage, f"Percentage distribution of {column}")


        # ANALYSE OF AV VALUES FOR PARAMETER
        message = ("Choose two columns for analyse of average value for parameter on dataset."
                   "\n(separate with comma - e.g.: 1,2)"
                   "\n[Type default for analysing average Total Revenue for Region - default dataset]")
        chosen_analyse_columns = self.choose_columns(dataframe_columns, column_index_strings, 2, message)
        if chosen_analyse_columns == "default":
            chosen_analyse_columns = ["Total Revenue", "Region"]
        print("___________________________")
        print(f"Plotting analyse of average value for parameter on dataset {given_dataset.get_filename()}.")
        average_value_per_parameter = given_dataset.get_processed_df().groupby(chosen_analyse_columns[1])[
            chosen_analyse_columns[0]].mean().reset_index()
        plot_module.make_sns_plot(average_value_per_parameter, chosen_analyse_columns[0], chosen_analyse_columns[1])


    def main(self):

        global datasets
        datasets = list()

        global chosen_dataset
        chosen_dataset = None

        builder = DatasetBuilder()

        print("> Data analysis tool <")
        print("by Aleksander Opalka PJATK")
        while True:

            try:
                user_input = self.show_main_menu()
            except Exception as e:
                print(f"Error occured: {e}")
                continue

            if user_input == "1":  # Load dataset
                try:
                    loaded_df, dataset_filename = self.load_dataset()
                    dataset_name = f"dataset_{len(datasets) + 1}"
                    tmp_dataset = builder.set_raw_df(loaded_df).set_name(dataset_name).set_filename(
                        dataset_filename).build()
                    datasets.append(tmp_dataset)
                    chosen_dataset = tmp_dataset
                except Exception as e:
                    print(f"Error occured: {e}")


            elif user_input == "2":  # Describe dataset
                try:
                    self.describe_dataset(chosen_dataset)
                except Exception as e:
                    print(f"Error while describing dataset: {e}")

            elif user_input == "3":  # Choose (change) dataset
                try:
                    chosen_dataset = self.choose_dataset()
                    print("Dataset chosen successully")
                except Exception as e:
                    print(f"Error while choosing dataset: {e}")

            elif user_input == "4":  # Perform data wrangling operations
                try:
                    self.perform_data_wrangling(chosen_dataset)
                except Exception as e:
                    print(f"Error while choosing dataset: {e}")

            elif user_input == "5":  # Run exploratory data analysis
                try:
                    self.perform_exploratory_data_analysis(chosen_dataset)
                except Exception as e:
                    print(f"Error while choosing dataset: {e}")

            elif user_input == 'Q':
                break

        print("Closing...")
        print("Closed.")
