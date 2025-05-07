import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('clean_online_retail.csv')

# Ensure 'Quantity' and 'UnitPrice' are numeric
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')

# Drop rows with missing or invalid numeric data
df.dropna(subset=['Quantity', 'UnitPrice'], inplace=True)

# Add 'TotalSales' column
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Convert 'InvoiceDate' to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create 'Month' column for monthly trends
df['Month'] = df['InvoiceDate'].dt.to_period('M')

# 1. Monthly Revenue Trend
monthly_revenue = df.groupby('Month')['TotalSales'].sum().reset_index()
monthly_revenue['Month'] = monthly_revenue['Month'].astype(str)

plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_revenue, x='Month', y='TotalSales', marker='o')
plt.title('Monthly Revenue Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Top 10 Products by Revenue
top_products = df.groupby('Description')['TotalSales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top 10 Products by Revenue')
plt.xlabel('Revenue')
plt.tight_layout()
plt.show()

# 3. Quantity vs Total Sales Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Quantity', y='TotalSales')
plt.title('Quantity vs Total Sales')
plt.tight_layout()
plt.show()
