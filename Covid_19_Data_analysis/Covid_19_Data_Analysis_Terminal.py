import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Day_19/country_wise_latest.csv")

# Data Cleaning
df = df.dropna(subset=["Country/Region"])
df = df.drop_duplicates()

# First 10 rows
data = df.head(10)

# Create 2 subplots
plt.figure(figsize=(14,6))

# Area Chart
plt.subplot(1, 2, 1)
plt.fill_between(
    data["Country/Region"],
    data["Recovered"]
)
plt.title("Recovered Cases (Area Chart)")
plt.xlabel("Country")
plt.ylabel("Recovered")
plt.xticks(rotation=45)

# Line Chart
plt.subplot(1, 2, 2)
plt.plot(
    data["Country/Region"],
    data["Deaths"],
    marker="o"
)
plt.title("Deaths (Line Chart)")
plt.xlabel("Country")
plt.ylabel("Deaths")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()