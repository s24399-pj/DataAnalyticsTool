import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def show_histogram(input_df: pd.DataFrame, columns_to_show: list):
    input_df[columns_to_show].hist(figsize=(10, 10))
    plt.show()

def make_pie_chart_percent(value_count_percentage: pd.Series, title: str):
    plt.pie(value_count_percentage.values, labels=value_count_percentage.index, autopct='%1.1f%%')
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

def make_bar_plot_counts(value_count: pd.Series, colors: list, title: str, x_name: str, y_name: str):
    bars = plt.bar(value_count.index, value_count.values, color=colors)
    plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .005, str(round(yval, 1)))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def make_sns_plot(data, value: str, parameter: str):
    # value = total rev
    plt.figure(figsize=(10, 6))
    sns.barplot(x=parameter, y=value, data=data, palette='viridis')
    plt.title(f"Average {value} by {parameter}")
    plt.xlabel(parameter)
    plt.ylabel(f"Average {value}")
    plt.show()
