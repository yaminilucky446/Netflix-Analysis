import pandas as pd
import matplotlib.pyplot as plt

# Read Netflix data
df = pd.read_csv("data/netflix_titles.csv")

# Show first rows
print(df.head())

# Create graph
df['type'].value_counts().plot(kind='bar')

plt.title("Movies vs TV Shows")

plt.show()