import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate


# Function to plot histograms for numerical variables
def plot_histograms(df):
    numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
    for col in numerical_cols:
        plt.figure(figsize=(8, 6))
        plt.hist(df[col], bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

# Function to plot bar charts for categorical variables
def plot_bar_charts(df):
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    for col in categorical_cols:
        plt.figure(figsize=(8, 6))
        df[col].value_counts().plot(kind='bar', color='skyblue')
        plt.title(f'Bar Chart of {col}')
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

# Function to plot histograms for a single numerical column
def plot_histogram(df, col):
    plt.figure(figsize=(8, 6))
    plt.hist(df[col], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Function to plot bar charts for a single categorical column
def plot_bar_chart(df, col):
    plt.figure(figsize=(8, 6))
    df[col].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f'Bar Chart of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def plot_time_series(df, time_col, value_col):
    plt.figure(figsize=(10, 6))
    plt.plot(df[time_col], df[value_col], color='skyblue')
    plt.title(f'Time Series Plot of {value_col}')
    plt.xlabel('Time')
    plt.ylabel(value_col)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

def plot_time_series_dots(df, time_col, value_col):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[time_col], df[value_col], color='skyblue', marker='o')
    plt.title(f'Time Series Plot with Dots of {value_col}')
    plt.xlabel('Time')
    plt.ylabel(value_col)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

def display_summary_table(data_summary):
    for col, summary in data_summary.items():
        print(f"\n{col}:\n{tabulate(summary.reset_index(), headers='keys', tablefmt='psql')}")


def scatter_plot(data, col_x, col_y):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=col_x, y=col_y, data=data)
    plt.title(f'Scatter Plot of {col_x} vs. {col_y}')
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.show()

def scatter_plot_advanced(data, col_x, col_y, hue):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=col_x, y=col_y, hue=hue, data=data)
    plt.title(f'Scatter Plot of {col_x} vs. {col_y} by {hue}')
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.show()

def box_plots(df):
    for column in df:
        plt.figure(figsize=(10, 5))
        sns.boxplot(x=df[column])
        plt.title(f'Box plot of {column}')
        plt.show()