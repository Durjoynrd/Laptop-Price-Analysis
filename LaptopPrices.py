import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the laptop prices dataset
df = pd.read_csv('laptop_prices.csv')

# Inspect the first few rows
print(df.head())
# Check for missing values
print(df.isnull().sum())
# Example: Fill missing values in 'Price_euros' with the average price
df['Price_euros'].fillna(df['Price_euros'].mean(), inplace=True)

# Remove rows where important columns like 'Ram' or 'OS' are missing
df.dropna(subset=['Ram', 'OS'], inplace=True)
# Descriptive statistics
print(df.describe())
# Group by company and calculate average price
avg_price_per_company = df.groupby('Company')['Price_euros'].mean()
print(avg_price_per_company)
# Bar plot for average price per company
plt.figure(figsize=(10,6))
sns.barplot(x=avg_price_per_company.index, y=avg_price_per_company.values)
plt.title('Average Laptop Price per Company')
plt.xticks(rotation=45)
plt.ylabel('Price in Euros')
plt.show()
