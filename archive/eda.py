# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Load the dataset
df = pd.read_csv('imdb_top_1000.csv')

# Filter out rows with unexpected values in 'Released_Year'
df = df[df['Released_Year'].str.isnumeric()]

# Convert 'Released_Year' to datetime format
df['Released_Year'] = pd.to_datetime(df['Released_Year'], errors='coerce', format='%Y')

# Drop rows with NaT (Not a Time) values in 'Released_Year'
df = df.dropna(subset=['Released_Year'])

# Set 'Released_Year' as the index
df.set_index('Released_Year', inplace=True)

# Display the first few rows of the dataset
print(df.head())

# EDA
# Distribution of Ratings
sns.histplot(df['IMDB_Rating'], bins=20, kde=True)
plt.title('Distribution of Movie Ratings')
plt.xlabel('IMDB Rating')
plt.ylabel('Frequency')
plt.show()

# Top Genres
top_genres = df['Genre'].value_counts().head(10)
top_genres.plot(kind='barh')
plt.title('Top 10 Movie Genres')
plt.xlabel('Number of Movies')
plt.ylabel('Genre')
plt.show()

# Top Directors
top_directors = df['Director'].value_counts().head(10)
top_directors.plot(kind='barh', color='orange')
plt.title('Top 10 Movie Directors')
plt.xlabel('Number of Movies Directed')
plt.ylabel('Director')
plt.show()

# Time Trend Analysis
plt.figure(figsize=(12, 6))
sns.lineplot(x=df.index, y=df['IMDB_Rating'], errorbar=None)

plt.title('Time Trend of IMDB Ratings Over Years')
plt.xlabel('Released Year')
plt.ylabel('IMDB Rating')
plt.show()

# Decomposition
result = seasonal_decompose(df['IMDB_Rating'], model='additive', period=1)
result.plot()
plt.suptitle('Seasonal Decomposition of IMDB Ratings Over Years', y=1.02)
plt.show()
