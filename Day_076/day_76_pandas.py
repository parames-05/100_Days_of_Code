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

cleandf['Starting Median Salary'].idxmin()

cleandf.loc[49]

