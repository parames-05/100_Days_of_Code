import pandas as pd

data = {
    "date": ["2026-01-01", "2026-01-01", "2026-01-02", "2026-01-02"],
    "product": ["Laptop", "Phone", "Laptop", "Phone"],
    "sales": [10, 15, 7, 20]
}

df = pd.DataFrame(data)

# Convert string → datetime
df["date"] = pd.to_datetime(df["date"])

print(df.dtypes)
pivot_df = df.pivot(
    index="date",
    columns="product",
    values="sales"
)

print(pivot_df)
df["timestamp"] = pd.to_datetime(
    ["2026-01-01 09:30", "2026-01-01 11:00",
     "2026-01-02 10:15", "2026-01-02 14:45"]
)

pivot_df = df.pivot(
    index="timestamp",
    columns="product",
    values="sales"
)