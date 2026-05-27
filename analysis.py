import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("data/netflix_titles.csv")

# Show first 5 rows
print(df.head())

# Count Movies vs TV Shows
df['type'].value_counts().plot(kind='bar')

plt.title("Movies vs TV Shows")

plt.show()
