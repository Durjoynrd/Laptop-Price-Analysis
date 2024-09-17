import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sample_sales_data.csv')
# Inspect the first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Fill missing values in 'sales' with the mean of the 'sales' column
df['sales'].fillna(df['sales'].mean(), inplace=True)
print(df.isnull().sum())  # Check if missing values are handled
# Group by region and calculate total sales
total_sales_per_region = df.groupby('region')['sales'].sum()
print(total_sales_per_region)
# Descriptive statistics
print(df.describe())
import matplotlib.pyplot as plt
import seaborn as sns

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Line plot for sales trends
sns.lineplot(x='date', y='sales', data=df, hue='region')
plt.title('Sales Trends Over Time by Region')
plt.show()


# Bar plot for sales by region and category
sns.barplot(x='region', y='sales', hue='category', data=df)
plt.title('Sales by Region and Category')
plt.show()
from scipy import stats

# Separate sales data for two regions
east_sales = df[df['region'] == 'East']['sales']
west_sales = df[df['region'] == 'West']['sales']

# Perform t-test
t_stat, p_val = stats.ttest_ind(east_sales, west_sales)
print(f"T-statistic: {t_stat}, P-value: {p_val}")

# Save the cleaned data
df.to_csv('cleaned_sales_data.csv', index=False)

