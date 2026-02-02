import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
data = {
    "date": [
        "2024-01-01", "2024-01-02", "2024-01-03",
        "2024-01-05", "2024-01-06", "2024-01-08",
        "2024-01-09", "2024-01-10"
    ],
    "value": [10, 12, None, 15, 14, None, 18, 20]
}

df = pd.DataFrame(data)

# -------------------------------
# 1. Data exploration
# -------------------------------
print("Head:")
print(df.head(), "\n")

print("Info:")
print(df.info(), "\n")

print("Missing values:")
print(df.isna().sum(), "\n")

# -------------------------------
# 2. Data cleaning
# -------------------------------
# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Set datetime index before interpolation
df = df.set_index("date")

# Handle missing values (time-series friendly)
df["value"] = df["value"].interpolate(method="time")

# -------------------------------
# 3. Resampling (Daily → Weekly mean)
# -------------------------------
weekly_df = df.resample("W").mean()

print("Weekly resampled data:")
print(weekly_df, "\n")

# -------------------------------
# 4. Time-series visualization
# -------------------------------
fig, ax = plt.subplots(figsize=(10, 5))

# Line plot with markers & style
ax.plot(
    weekly_df.index,
    weekly_df["value"],
    linestyle="--",
    marker="o",
    linewidth=2,
    markersize=6,
    label="Weekly Average"
)

# -------------------------------
# 5. Date locators & formatters
# -------------------------------
# Major ticks: weekly
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))

# Minor ticks: daily
ax.xaxis.set_minor_locator(mdates.DayLocator())

# Date formatting
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d, %Y"))

# Rotate dates
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

# -------------------------------
# 6. Grid & styling
# -------------------------------
ax.grid(True, which="major", linestyle="-", linewidth=0.7)
ax.grid(True, which="minor", linestyle=":", linewidth=0.4)

ax.set_title("Weekly Time Series Analysis")
ax.set_xlabel("Date")
ax.set_ylabel("Value")

ax.legend()

plt.tight_layout()
plt.show()

