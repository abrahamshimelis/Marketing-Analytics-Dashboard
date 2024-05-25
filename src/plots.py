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

def plot_bar_chart_for_cols(df, num_column, cat_column):
    # Group by category and sum the numerical values
    df_grouped = df.groupby(cat_column)[num_column].sum().reset_index()

    # Plot the bar chart for the total numerical values per category
    plt.figure(figsize=(10, 6))  # Create a new figure with a specific size (optional)
    plt.bar(df_grouped[cat_column], df_grouped[num_column], color='blue', alpha=0.7)  # Plot the bar chart
    plt.xlabel(cat_column)  # Label for the x-axis
    plt.ylabel('Total ' + num_column)  # Label for the y-axis
    plt.title('Total ' + num_column + ' Per ' + cat_column)  # Title of the plot
    plt.xticks(rotation=90)  # Rotate the x-axis labels if they are long
    plt.grid(True)  # Show the grid (optional)
    plt.show()  # Display the plot

def plot_time_series(df, date_column, value_column):
    # Group by date and sum the values
    df_grouped = df.groupby(date_column)[value_column].sum().reset_index()

    # Plot the line chart for the total values per date
    plt.figure(figsize=(10, 6))  # Create a new figure with a specific size (optional)
    plt.plot(df_grouped[date_column], df_grouped[value_column], label=value_column)  # Plot the line chart
    plt.xlabel('Date')  # Label for the x-axis
    plt.ylabel('Total ' + value_column)  # Label for the y-axis
    plt.title('Total ' + value_column + ' Over Time')  # Title of the plot
    plt.legend()  # Show the legend
    plt.grid(True)  # Show the grid (optional)
    plt.show()  # Display the plot

def plot_time_series_by_category(df, date_column, value_column, category_column):
    # Create a new figure with a specific size (optional)
    plt.figure(figsize=(10, 6))

    # Get the unique categories
    categories = df[category_column].unique()

    # For each category
    for category in categories:
        # Filter the DataFrame for the category
        df_filtered = df[df[category_column] == category]

        # Group by date and sum the values
        df_grouped = df_filtered.groupby(date_column)[value_column].sum().reset_index()

        # Plot the line chart for the total values per date
        plt.plot(df_grouped[date_column], df_grouped[value_column], label=category)

    # Set the labels and title
    plt.xlabel('Date')  # Label for the x-axis
    plt.ylabel('Total ' + value_column)  # Label for the y-axis
    plt.title('Total ' + value_column + ' Over Time by ' + category_column)  # Title of the plot

    # Show the legend and grid
    plt.legend()  # Show the legend
    plt.grid(True)  # Show the grid (optional)

    # Display the plot
    plt.show()

def plot_time_series_for_single_category(df, date_column, value_column, category_column, category_value):
    # Filter the DataFrame for the category
    df_filtered = df[df[category_column] == category_value]

    # Group by date and sum the values
    df_grouped = df_filtered.groupby(date_column)[value_column].sum().reset_index()

    # Plot the line chart for the total values per date
    plt.figure(figsize=(10, 6))  # Create a new figure with a specific size (optional)
    plt.plot(df_grouped[date_column], df_grouped[value_column], label=category_value)  # Plot the line chart
    plt.xlabel('Date') 
    plt.ylabel('Total ' + value_column) 
    plt.title('Total ' + value_column + ' Over Time for ' + category_value)
    plt.legend() 
    plt.grid(True) 
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