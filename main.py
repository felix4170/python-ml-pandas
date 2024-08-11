# import requests

import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('sales_data.csv')

# Display basic information about the data
print("Data Information:")
print(data.info())

print("\nFirst few rows of the data:")
print(data.head())

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Calculate total sales per product
sales_per_product = data.groupby('Product')['Sales'].sum().reset_index()

print("\nTotal Sales per Product:")
print(sales_per_product)

# Calculate daily sales
daily_sales = data.groupby('Date')['Sales'].sum().reset_index()

print("\nDaily Sales:")
print(daily_sales)

# Plot total sales per product
plt.figure(figsize=(10, 6))
plt.bar(sales_per_product['Product'], sales_per_product['Sales'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Total Sales per Product')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('total_sales_per_product.png')
plt.show()

# Plot daily sales
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['Date'], daily_sales['Sales'], marker='o', linestyle='-', color='coral')
plt.xlabel('Date')
plt.ylabel('Daily Sales')
plt.title('Daily Sales Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_sales.png')
plt.show()