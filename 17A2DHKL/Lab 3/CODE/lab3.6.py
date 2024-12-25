import pandas as pd

# Load data
DataFrame_stock1 = pd.read_csv('DATA/stocks1.csv')
DataFrame_stock2 = pd.read_csv('DATA/stocks2.csv')

# Concatenate the two dataframes
stocks = pd.concat([DataFrame_stock1, DataFrame_stock2], ignore_index=True)

# Create a pivot table
bang_tong_hop = stocks.pivot_table(
    values='close',
    index='date',
    columns='symbol',
    aggfunc='mean'
)

# Calculate the total volume for each symbol
tong_volume = stocks.groupby('symbol')['volume'].sum()

# Add 'tong_volume' as a new row for sorting
bang_tong_hop.loc['tong_volume'] = bang_tong_hop.columns.map(tong_volume)

# Sort columns by 'tong_volume'
bang_tong_hop_sorted = bang_tong_hop.sort_values(by='tong_volume', axis=1, ascending=False)

# Drop 'tong_volume' row after sorting
bang_tong_hop_sorted = bang_tong_hop_sorted.drop(index='tong_volume')

# Print the result
print(bang_tong_hop_sorted.head())
