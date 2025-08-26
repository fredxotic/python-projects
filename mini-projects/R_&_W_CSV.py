import pandas as pd
csv_data = pd.read_csv("data.csv")
print("CSV Data:")
print(csv_data)

# Write the DataFrame to an Excel file
csv_data.to_excel("data_output.xlsx", index=False)

# Read the Excel file
excel_data = pd.read_excel("data_output.xlsx")
print("\nExcel Data:")
print(excel_data)
