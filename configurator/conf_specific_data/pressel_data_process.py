import pandas as pd

# Load the Excel file (either .xls or .xlsx)
df = pd.read_excel('configurator/conf_specific_data/pressel_list.xlsx')

# Perform operations on the DataFrame
lst = df['Type'].unique()

for item in lst:
    print(item.upper())

