import pandas as pd

df = pd.read_csv("../data/raw/SuperMarket Analysis.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month_name()
df["Day"] = df["Date"].dt.day_name()
df["Year"] = df["Date"].dt.year

df.to_csv("../data/processed/cleaned_supermarket.csv", index=False)

sales_summary = df.groupby("Product line")["Sales"].sum()

sales_summary.to_csv("../reports/product_sales_summary.csv")

print("Automation completed successfully.")