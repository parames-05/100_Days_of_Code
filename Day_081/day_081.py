import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

search_df = pd.read_csv("Bitcoin Search Trend.csv")
price_df = pd.read_csv("Daily Bitcoin Price.csv")

print("Initial Search Columns:", search_df.columns)
print("Initial Price Columns:", price_df.columns)
search_df.columns = search_df.columns.str.strip().str.upper()
price_df.columns = price_df.columns.str.strip().str.upper()

print("\nStandardized Search Columns:", search_df.columns)
print("Standardized Price Columns:", price_df.columns)
search_df['DATE'] = pd.to_datetime(search_df.iloc[:, 0], errors='coerce')
price_df['DATE'] = pd.to_datetime(price_df.iloc[:, 0], errors='coerce')
search_df['BITCOIN_SEARCH'] = pd.to_numeric(
    search_df.iloc[:, 1], errors='coerce'
)

price_df['CLOSE'] = price_df.iloc[:, 1].astype(str).str.replace(",", "")
price_df['CLOSE'] = pd.to_numeric(price_df['CLOSE'], errors='coerce')


search_df = search_df.dropna(subset=['DATE', 'BITCOIN_SEARCH'])
price_df = price_df.dropna(subset=['DATE', 'CLOSE'])

print("\nCleaned Search Data:")
print(search_df.head())

print("\nCleaned Price Data:")
print(price_df.head())


merged_df = pd.merge(
    search_df[['DATE', 'BITCOIN_SEARCH']],
    price_df[['DATE', 'CLOSE']],
    on='DATE',
    how='inner'
)

print("\nMerged Data Preview:")
print(merged_df.head())

merged_df.set_index('DATE', inplace=True)

monthly_df = merged_df.resample('M').mean().reset_index()

print("\nMonthly Aggregated Data:")
print(monthly_df.head())


correlation = monthly_df['BITCOIN_SEARCH'].corr(monthly_df['CLOSE'])

print("\nCorrelation between Search Interest and Bitcoin Price:")
print(round(correlation, 4))

median_search = monthly_df['BITCOIN_SEARCH'].median()

monthly_df['INTEREST_LEVEL'] = np.where(
    monthly_df['BITCOIN_SEARCH'] >= median_search,
    "High Interest",
    "Low Interest"
)

interest_counts = (
    monthly_df['INTEREST_LEVEL']
    .value_counts()
    .reset_index()
)

interest_counts.columns = ['INTEREST_LEVEL', 'COUNT']

print("\nInterest Distribution:")
print(interest_counts)
price_threshold = monthly_df['CLOSE'].quantile(0.80)

monthly_df['PRICE_SPIKE'] = np.where(
    monthly_df['CLOSE'] >= price_threshold,
    1,
    0
)

spike_correlation = monthly_df['BITCOIN_SEARCH'].corr(
    monthly_df['PRICE_SPIKE']
)

print("\nCorrelation between Search Interest and Price Spikes:")
print(round(spike_correlation, 4))



pie_fig = px.pie(
    interest_counts,
    names='INTEREST_LEVEL',
    values='COUNT',
    title='Distribution of High vs Low Bitcoin Search Interest (Monthly)',
)

pie_fig.update_traces(textposition='inside', textinfo='percent+label')
pie_fig.show()

donut_fig = go.Figure(
    data=[
        go.Pie(
            labels=interest_counts['INTEREST_LEVEL'],
            values=interest_counts['COUNT'],
            hole=0.5
        )
    ]
)

donut_fig.update_layout(
    title_text='Donut Chart: Bitcoin Search Interest Distribution',
    annotations=[dict(text='BTC<br>Interest', x=0.5, y=0.5, font_size=16, showarrow=False)]
)

donut_fig.show()


print("\n--- DAY 1 ANALYSIS COMPLETE ---")

if correlation > 0.6:
    print("Strong positive correlation: Search interest closely tracks price.")
elif correlation > 0.3:
    print("Moderate correlation: Search interest partially tracks price.")
else:
    print("Weak correlation: Search interest may lag or behave independently.")

print("\nBehavioral Insight:")
print("Google search interest may reflect speculative excitement cycles.")
