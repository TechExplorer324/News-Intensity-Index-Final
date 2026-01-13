import pandas as pd

# Create date range
dates = pd.date_range(start="2024-01-11", end="2024-12-01", freq="D")

# Format dates as DD-MM-YYYY
df = pd.DataFrame({
    "Date": dates.strftime("%d-%m-%Y")
})

# Save to Excel
df.to_excel("trial.xlsx", index=False)

print("trial.xlsx created successfully.")