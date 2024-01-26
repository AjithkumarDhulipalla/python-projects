import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('medical_examination.csv')

# Add overweight column
df['overweight'] = None  # Set to 0 or 1 based on BMI calculation

# Normalize data
# ...

# Clean data
df = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & ...]

# Create categorical features chart
# ...

# Create correlation matrix
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", mask=correlation_matrix <= 0.0)

# Show the plots
plt.show()
