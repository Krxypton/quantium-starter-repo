import pandas as pd

# Load all 3 CSVs
df = pd.concat([
    pd.read_csv('data/daily_sales_data_0.csv'),
    pd.read_csv('data/daily_sales_data_1.csv'),
    pd.read_csv('data/daily_sales_data_2.csv'),
])

# Filter to Pink Morsels only
df = df[df['product'] == 'pink morsel']

# Create sales column
df['sales'] = df['quantity'] * df['price']

# Keep only the required columns
df = df[['sales', 'date', 'region']]

# Save to output file
df.to_csv('data/output.csv', index=False)

print("Done!")