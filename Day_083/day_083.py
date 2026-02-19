import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# 1. LOAD DATASETS
# ---------------------------------------------------

df_pre = pd.read_csv("UE Benefits Search vs UE Rate 2004-19.csv")
df_post = pd.read_csv("UE Benefits Search vs UE Rate 2004-20.csv")

print("Pre-2020 Columns:", df_pre.columns)
print("Post-2020 Columns:", df_post.columns)

# ---------------------------------------------------
# 2. STANDARDIZE COLUMN NAMES
# ---------------------------------------------------

df_pre.columns = df_pre.columns.str.strip().str.upper()
df_post.columns = df_post.columns.str.strip().str.upper()


# ---------------------------------------------------
# 3. CLEAN FUNCTION (Reusable)
# ---------------------------------------------------

def clean_dataset(df):
    df = df.copy()

    # Assume first column is Date
    df['DATE'] = pd.to_datetime(df.iloc[:, 0], errors='coerce')

    # Assume second column is Search Interest
    df['UE_SEARCH'] = pd.to_numeric(df.iloc[:, 1], errors='coerce')

    # Assume third column is Unemployment Rate
    df['UE_RATE'] = (
        df.iloc[:, 2]
        .astype(str)
        .str.replace(",", "", regex=True)
    )
    df['UE_RATE'] = pd.to_numeric(df['UE_RATE'], errors='coerce')

    # Drop invalid rows
    df = df.dropna(subset=['DATE', 'UE_SEARCH', 'UE_RATE'])

    # Sort
    df = df.sort_values('DATE')

    return df[['DATE', 'UE_SEARCH', 'UE_RATE']]


df_pre = clean_dataset(df_pre)
df_post = clean_dataset(df_post)

print("\nCleaned Pre-2020 Preview:")
print(df_pre.head())

print("\nCleaned Post-2020 Preview:")
print(df_post.head())

# ---------------------------------------------------
# 4. CORRELATION ANALYSIS
# ---------------------------------------------------

corr_pre = df_pre['UE_SEARCH'].corr(df_pre['UE_RATE'])
corr_post = df_post['UE_SEARCH'].corr(df_post['UE_RATE'])

print("\nCorrelation (2004-2019):", round(corr_pre, 4))
print("Correlation (2004-2020):", round(corr_post, 4))

# ---------------------------------------------------
# 5. MERGE FOR COMPARISON
# ---------------------------------------------------

df_pre['PERIOD'] = '2004-2019'
df_post['PERIOD'] = '2004-2020'

combined_df = pd.concat([df_pre, df_post], ignore_index=True)

# ---------------------------------------------------
# 6. BOXPLOT – DISTRIBUTION SHIFT
# ---------------------------------------------------

box_fig = px.box(
    combined_df,
    x='PERIOD',
    y='UE_SEARCH',
    title='Distribution of Unemployment Search Interest (Pre vs Including 2020)',
    points='outliers'
)

box_fig.show()

# ---------------------------------------------------
# 7. SCATTER COMPARISON
# ---------------------------------------------------

scatter_fig = go.Figure()

scatter_fig.add_trace(
    go.Scatter(
        x=df_pre['UE_SEARCH'],
        y=df_pre['UE_RATE'],
        mode='markers',
        name='2004-2019'
    )
)

scatter_fig.add_trace(
    go.Scatter(
        x=df_post['UE_SEARCH'],
        y=df_post['UE_RATE'],
        mode='markers',
        name='2004-2020'
    )
)

scatter_fig.update_layout(
    title='Search Interest vs Unemployment Rate (Pre vs Including 2020)',
    xaxis_title='Google Search Interest (UE Benefits)',
    yaxis_title='Unemployment Rate (%)'
)

scatter_fig.show()

# ---------------------------------------------------
# 8. VOLATILITY CHECK
# ---------------------------------------------------

df_post['SEARCH_VOLATILITY'] = df_post['UE_SEARCH'].pct_change()

volatility_correlation = df_post['SEARCH_VOLATILITY'].corr(df_post['UE_RATE'])

print("\nCorrelation (Search Volatility vs UE Rate - Post Dataset):",
      round(volatility_correlation, 4))

# ---------------------------------------------------
# 9. MONTHLY AVERAGE TREND
# ---------------------------------------------------

df_post.set_index('DATE', inplace=True)

monthly_post = df_post.resample('M').mean().reset_index()

line_fig = go.Figure()

line_fig.add_trace(
    go.Scatter(
        x=monthly_post['DATE'],
        y=monthly_post['UE_SEARCH'],
        mode='lines',
        name='Avg Monthly Search'
    )
)

line_fig.add_trace(
    go.Scatter(
        x=monthly_post['DATE'],
        y=monthly_post['UE_RATE'],
        mode='lines',
        name='Avg Monthly UE Rate'
    )
)

line_fig.update_layout(
    title='Monthly Unemployment Search vs Unemployment Rate (Including 2020)'
)

line_fig.show()

# ---------------------------------------------------
# 10. FINAL SUMMARY
# ---------------------------------------------------

print("\n--- DAY 3 ANALYSIS COMPLETE ---")

if corr_post > corr_pre:
    print("Correlation strengthened when 2020 was included.")
    print("Economic shock amplified search-rate alignment.")
else:
    print("Correlation did not significantly strengthen post-2020.")

print("\nInterpretation:")
print("Search interest behaves like a real-time anxiety sensor.")
print("2020 introduced extreme outliers, visible in boxplot expansion.")
print("Digital search data can act as a macroeconomic early signal.")
