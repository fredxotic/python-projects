import pandas as pd
import datetime

# Starting balance
starting_balance = 10000

# Assume semester months: September, October, November, December (4 months)
months = ["September", "October", "November", "December"]
days_in_month = [30, 31, 30, 31]  # approximate days

# Daily spend assumption
daily_spend = 90

# Calculate monthly planned spend and remaining balance
balance = starting_balance
records = []

for month, days in zip(months, days_in_month):
    spend = days * daily_spend
    end_balance = balance - spend
    records.append({
        "Month": month,
        "Days": days,
        "Planned Spend (KSh)": spend,
        "Start Balance (KSh)": balance,
        "End Balance (KSh)": end_balance
    })
    balance = end_balance

# Create DataFrame
df_budget = pd.DataFrame(records)
print("Semester Budget Tracker")
print(df_budget)


