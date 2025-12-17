import pandas as pd
import matplotlib.pyplot as plt

# 1. Create Sample Data

data = { 'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
         'Sales': [15000, 18000, 22000, 21000, 25000, 27000],
         'Target': [16000, 17000, 20000, 22000, 24000, 26000],
         'Customers': [120, 150, 170, 160, 200, 220],
         'Electronics': [6000, 7000, 9000, 8000, 10000, 11000],
         'Clothing': [4000, 5000, 6000, 5500, 6500, 7000],
         'Books': [3000, 4000, 5000, 4500, 6000, 6500] }
df = pd.DataFrame(data)

# 2. Monthly Sales Trend

plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linewidth=2, label='Actual Sales')
plt.plot(df['Month'], df['Target'], marker='s', linestyle='--', linewidth=2, label='Target Sales')

# Annotation for highest sales

max_sales = df['Sales'].max()
max_month = df.loc[df['Sales'].idxmax(), 'Month']
plt.annotate(f'Highest Sales: ₹{max_sales}', xy=(max_month, max_sales), xytext=(max_month, max_sales - 5000), arrowprops=dict(arrowstyle='->'))

plt.title('Monthly Sales vs Target', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (₹)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig('sales_trend.png')
plt.show()

# 3. Product Category Sales Distribution

categories = ['Electronics', 'Clothing', 'Books']
latest_sales = [df['Electronics'].iloc[-1],
                df['Clothing'].iloc[-1],
                df['Books'].iloc[-1]]
explode = (0.1, 0, 0)

plt.figure(figsize=(8, 8))
plt.pie(latest_sales, labels=categories, autopct='%1.1f%%', explode=explode, shadow=True, startangle=140)

plt.title('Product Category Sales Share (June)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('category_distribution.png')
plt.show()

# 4. Monthly Customer Growth

plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Customers'], alpha=0.7)

# Highlight highest growth month

max_customers = df['Customers'].max()
max_cust_month = df.loc[df['Customers'].idxmax(), 'Month']
plt.annotate(f'Peak: {max_customers}', xy=(max_cust_month, max_customers), xytext=(max_cust_month, max_customers - 60), arrowprops=dict(arrowstyle='->'))

plt.title('Monthly Customer Growth', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('customer_growth.png')
plt.show()

print('Dashboard plots generated and saved successfully.')
