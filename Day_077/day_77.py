import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
df.head()

df.shape

df.columns

df.isna()

cleandf=df.dropna()
cleandf['Starting Median Salary']
cleandf['Starting Median Salary'].max()
cleandf['Starting Median Salary'].idxmax()
cleandf['Group'].loc[43]

cleandf['Starting Median Salary'].max()

cleandf['Starting Median Salary'].idxmax()

cleandf.loc[43]

cleandf['Mid-Career Median Salary'].idxmax()

cleandf.loc[8]

cleandf.loc[49]

cleandf['Starting Median Salary'].idxmin()

spread_col = cleandf["Mid-Career 90th Percentile Salary"] - cleandf["Mid-Career 10th Percentile Salary"]
cleandf.insert(1,"Spread",spread_col)
cleandf.head(6)

low_risk= cleandf.sort_values('Spread')

print(low_risk)

pd.options.display.float_format = '{:,.2f}'.format

group_cnt = cleandf.groupby("Group").count()
print(group_cnt)

