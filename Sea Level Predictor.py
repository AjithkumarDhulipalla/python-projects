import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load data
df = pd.read_csv('epa-sea-level.csv')

# Create Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Linear Regression and Plot for the entire dataset
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.plot(df['Year'], intercept + slope * df['Year'], color='red', label='Entire Dataset')

# Linear Regression and Plot for recent years (2000 onwards)
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
plt.plot(recent_data['Year'], intercept_recent + slope_recent * recent_data['Year'], color='blue', label='2000 Onwards')

# Set legend
plt.legend()

# Save and return the image
plt.savefig('sea_level_plot.png')
plt.show()
