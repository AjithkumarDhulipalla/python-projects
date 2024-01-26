import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
# ...

# Draw Line Plot
def draw_line_plot():
    plt.figure(figsize=(10, 6))
    # Use plt.plot() to create the line chart
    # Set title, x-axis label, y-axis label
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    # Save and return the image
    plt.savefig('line_plot.png')
    return plt.gcf()

# Draw Bar Plot
def draw_bar_plot():
    plt.figure(figsize=(12, 8))
    # Use sns.barplot() to create the bar chart
    # Set legend, x-axis label, y-axis label
    plt.title("Months Average Page Views (2016-2019)")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    # Save and return the image
    plt.savefig('bar_plot.png')
    return plt.gcf()

# Draw Box Plot
def draw_box_plot():
    # Prepare data for box plots
    plt.figure(figsize=(14, 8))
    # Use sns.boxplot() to create the box plots
    # Set titles, x-axis label, y-axis label
    plt.suptitle("Year-wise and Month-wise Box Plots")
    plt.xlabel("Years/Months")
    plt.ylabel("Page Views")
    # Save and return the image
    plt.savefig('box_plot.png')
    return plt.gcf()

# Run and test your functions using main.py
