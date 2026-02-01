import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

colors = pd.read_csv('LEGO Notebook and Data (completed)/data/colors.csv')
sets = pd.read_csv('LEGO Notebook and Data (completed)/data/sets.csv')
themes = pd.read_csv('LEGO Notebook and Data (completed)/data/themes.csv')

print("Colors DataFrame Head:")
display(colors.head())
print("\nSets DataFrame Head:")
display(sets.head())
print("\nThemes DataFrame Head:")
display(themes.head())

"""### Data Information and Missing Values"""

print("Colors DataFrame Info:")
colors.info()
print("\nSets DataFrame Info:")
sets.info()
print("\nThemes DataFrame Info:")
themes.info()

print("Missing values in Colors:")
display(colors.isnull().sum())
print("\nMissing values in Sets:")
display(sets.isnull().sum())
print("\nMissing values in Themes:")
display(themes.isnull().sum())

sets['year'] = sets['year'].astype(int)

# Merge datasets
# Merge sets with themes to get theme names
sets_with_themes = pd.merge(sets, themes, left_on='theme_id', right_on='id', suffixes=('_set', '_theme'))

# Merge sets_with_themes with colors to get color names (for parts, not sets directly)
# This step is more complex as set-color relationship is not directly in 'sets.csv'
# For this notebook, we'll focus on set-theme and overall color distribution.

print("Merged Sets with Themes DataFrame Head:")
display(sets_with_themes.head())

sets_per_year = sets.groupby('year')['set_num'].count().reset_index()
sets_per_year.columns = ['year', 'num_sets']

plt.figure(figsize=(14, 7))
sns.lineplot(x='year', y='num_sets', data=sets_per_year)
plt.title('Number of LEGO Sets Released Over Time', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Sets', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""### Top 10 LEGO Themes by Number of Sets"""

top_themes = sets_with_themes['name_theme'].value_counts().head(10).reset_index()
top_themes.columns = ['theme_name', 'num_sets']

plt.figure(figsize=(14, 7))
sns.barplot(x='theme_name', y='num_sets', data=top_themes, palette='viridis')
plt.title('Top 10 LEGO Themes by Number of Sets', fontsize=16)
plt.xlabel('Theme Name', fontsize=12)
plt.ylabel('Number of Sets', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""### Distribution of Transparent Colors"""

transparent_colors = colors[colors['is_trans'] == True]

plt.figure(figsize=(10, 8))
sns.countplot(y='name', data=transparent_colors, order=transparent_colors['name'].value_counts().index, palette='plasma')
plt.title('Distribution of Transparent LEGO Colors', fontsize=16)
plt.xlabel('Count', fontsize=12)
plt.ylabel('Color Name', fontsize=12)
plt.tight_layout()
plt.show()

"""## 4. Advanced Analysis: Sets per Theme per Year

Let's investigate how the number of sets for certain themes has evolved over time. This can show the longevity and popularity trends of different LEGO lines.
"""

sets_per_theme_year = sets_with_themes.groupby(['name_theme', 'year']).count()['set_num'].reset_index()
sets_per_theme_year.columns = ['theme_name', 'year', 'num_sets']

# Filter for some popular themes to visualize trends
popular_themes = ['Star Wars', 'Technic', 'City', 'Friends', 'Creator']
filtered_themes_data = sets_per_theme_year[sets_per_theme_year['theme_name'].isin(popular_themes)]

plt.figure(figsize=(16, 9))
sns.lineplot(x='year', y='num_sets', hue='theme_name', data=filtered_themes_data, marker='o')
plt.title('Number of LEGO Sets per Popular Theme Over Time', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Sets', fontsize=12)
plt.legend(title='Theme')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
