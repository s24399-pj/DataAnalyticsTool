# Data Analysis Tool - Aleksander Opałka - s24399

## Overview
This python data analysis tool with functionalities for loading datasets, performing data wrangling operations, and conducting exploratory data analysis.
 The project includes a command-line user interface for interacting with the tool.

## Modules

### analyse_module.py

- provides a comprehensive summary of a DataFrame, including its head, dimensions, null values, data types, uniqueness of the ID column, percentage of unique values, and basic descriptive statistics.

### operations_module.py

- The load_data function loads a dataset from a specified CSV file path, using a given separator, and returns it as a DataFrame. It constructs the full file path, reads the CSV file into a DataFrame, and handles any exceptions that occur during the loading process by raising a descriptive error.

### wrangle_module.py

- The module provides three data wrangling functions: drop_and_count_duplicate_rows, which removes duplicate rows from a DataFrame and returns the cleaned DataFrame along with the count of removed duplicates; drop_and_count_NA_values, which removes rows with missing values from a DataFrame and returns the cleaned DataFrame along with the count of removed rows; and date_columns_to_datetime, which converts columns containing "date" in their name to datetime format in the DataFrame.

### plot_module.py

- **show_histogram** generates and displays histograms for specified columns in a DataFrame.
- **make_pie_chart_percent** creates and displays a pie chart showing percentage distribution of values from a given Series with a specified title.
- **make_bar_plot_counts** creates and displays a bar plot for value counts from a Series, with specified colors, title, and axis labels, and annotates each bar with its height.
- **make_sns_plot** uses Seaborn to create and display a bar plot showing the average of a specified value grouped by a specified parameter, with appropriate titles and labels.


### dataset.py

- The Dataset class encapsulates a dataset with its raw and processed DataFrames, as well as its name and filename. It provides methods to retrieve the raw DataFrame (get_raw_df), dataset name (get_name), filename (get_filename), and processed DataFrame (get_processed_df). Additionally, it allows setting a new processed DataFrame using the set_processed_df method.

### dataset_builder.py

- The DatasetBuilder class is a builder pattern implementation for creating Dataset objects. It allows for step-by-step construction of a Dataset by setting its raw DataFrame (set_raw_df), name (set_name), and filename (set_filename). After all necessary attributes are set, the build method constructs and returns a Dataset object. If any required attribute is missing, the build method raises a ValueError.
