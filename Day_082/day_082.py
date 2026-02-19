import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# ---------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------

df = pd.read_csv("TESLA Search Trend vs Price.csv")

print("Initial Columns:", df.columns)


# ---------------------------------------------------
# 2. STANDARDIZE & CLEAN
# ---------------------------------------------------

# Clean column names
df.columns = df.columns.str.strip().str.upper()

print("Standardized Columns:", df.columns)

# Extract date (assume first column)
df['DATE'] = pd.to_datetime(df.iloc[:, 0], errors='coerce')

# Extract search interest (assume second column)
df['TESLA_SEARCH'] = pd.to_numeric(df.iloc[:, 1], errors='coerce')

# Extract price (assume third column)
df['TESLA_PRICE'] = (
    df.iloc[:, 2]
    .astype(str)
    .str.replace(",", "", regex=True)
)

df['TESLA_PRICE'] = pd.to_numeric(df['TESLA_PRICE'], errors='coerce')

# Remove invalid rows
df = df.dropna(subset=['DATE', 'TESLA_SEARCH', 'TESLA_PRICE'])

df = df.sort_values('DATE')

print("\nCleaned Data Preview:")
print(df.head())


# ---------------------------------------------------
# 3. ROLLING AVERAGES (30-DAY)
# ---------------------------------------------------

df.set_index('DATE', inplace=True)

df['SEARCH_ROLLING_30'] = df['TESLA_SEARCH'].rolling(window=30).mean()
df['PRICE_ROLLING_30'] = df['TESLA_PRICE'].rolling(window=30).mean()

df.reset_index(inplace=True)


# ---------------------------------------------------
# 4. CORRELATION ANALYSIS
# ---------------------------------------------------

correlation = df['TESLA_SEARCH'].corr(df['TESLA_PRICE'])
print("\nCorrelation (Search vs Price):", round(correlation, 4))


# ---------------------------------------------------
# 5. SCATTER WITH MANUAL TRENDLINE
# ---------------------------------------------------

# Linear regression using NumPy
coefficients = np.polyfit(df['TESLA_SEARCH'], df['TESLA_PRICE'], 1)
trend_function = np.poly1d(coefficients)

df['TRENDLINE'] = trend_function(df['TESLA_SEARCH'])

scatter_fig = go.Figure()

scatter_fig.add_trace(
    go.Scatter(
        x=df['TESLA_SEARCH'],
        y=df['TESLA_PRICE'],
        mode='markers',
        name='Data Points'
    )
)

scatter_fig.add_trace(
    go.Scatter(
        x=df['TESLA_SEARCH'],
        y=df['TRENDLINE'],
        mode='lines',
        name='Trendline'
    )
)

scatter_fig.update_layout(
    title='Tesla Search Interest vs Tesla Stock Price',
    xaxis_title='Google Search Interest',
    yaxis_title='Tesla Stock Price'
)

scatter_fig.show()


# ---------------------------------------------------
# 6. BAR CHART – HIGH vs LOW SEARCH
# ---------------------------------------------------

median_search = df['TESLA_SEARCH'].median()

df['SEARCH_CATEGORY'] = np.where(
    df['TESLA_SEARCH'] >= median_search,
    'High Search',
    'Low Search'
)

avg_price_by_search = (
    df.groupby('SEARCH_CATEGORY')['TESLA_PRICE']
    .mean()
    .reset_index()
)

bar_fig = px.bar(
    avg_price_by_search,
    x='SEARCH_CATEGORY',
    y='TESLA_PRICE',
    title='Average Tesla Price During High vs Low Search Periods',
    labels={'TESLA_PRICE': 'Average Stock Price'}
)

bar_fig.show()


# ---------------------------------------------------
# 7. GROUPED BAR – MONTHLY COMPARISON
# ---------------------------------------------------

df['MONTH'] = df['DATE'].dt.to_period('M')

monthly_grouped = (
    df.groupby('MONTH')[['TESLA_SEARCH', 'TESLA_PRICE']]
    .mean()
    .reset_index()
)

monthly_grouped['MONTH'] = monthly_grouped['MONTH'].astype(str)

grouped_bar = go.Figure()

grouped_bar.add_trace(
    go.Bar(
        x=monthly_grouped['MONTH'],
        y=monthly_grouped['TESLA_SEARCH'],
        name='Avg Search Interest'
    )
)

grouped_bar.add_trace(
    go.Bar(
        x=monthly_grouped['MONTH'],
        y=monthly_grouped['TESLA_PRICE'],
        name='Avg Price'
    )
)

grouped_bar.update_layout(
    barmode='group',
    title='Monthly Average Tesla Search vs Price'
)

grouped_bar.show()


# ---------------------------------------------------
# 8. VOLATILITY ANALYSIS
# ---------------------------------------------------

df['PRICE_VOLATILITY'] = df['TESLA_PRICE'].pct_change()

volatility_corr = df['TESLA_SEARCH'].corr(df['PRICE_VOLATILITY'])

print("Correlation (Search vs Volatility):", round(volatility_corr, 4))


# ---------------------------------------------------
# 9. FINAL SUMMARY
# ---------------------------------------------------

print("\n--- DAY 2 ANALYSIS COMPLETE ---")

if correlation > 0.6:
    print("Strong relationship: search behavior closely aligns with price.")
elif correlation > 0.3:
    print("Moderate relationship: hype and price partially move together.")
else:
    print("Weak relationship: price may drive search more than search drives price.")

print("\nInterpretation:")
print("Search spikes often cluster around volatile periods.")
print("Retail curiosity appears to amplify market momentum rather than create it from nothing.")
