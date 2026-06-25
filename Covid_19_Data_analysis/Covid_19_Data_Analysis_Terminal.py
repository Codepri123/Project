# import pandas as pd
# import matplotlib.pyplot as plt

# # Load dataset
# df = pd.read_csv("Day_19/country_wise_latest.csv")

# # Data Cleaning
# df = df.dropna(subset=["Country/Region"])
# df = df.drop_duplicates()

# # Take first 10 countries to avoid crowded graph
# data = df.head(10)

# # Create figure
# plt.figure(figsize=(12, 6))

# # Area Chart for Recovered Cases
# plt.fill_between(
#     data["Country/Region"],
#     data["Recovered"],
#     alpha=0.5,
#     label="Recovered Cases"
# )

# # Line Chart for Death Cases
# plt.plot(
#     data["Country/Region"],
#     data["Deaths"],
#     marker="o",
#     linewidth=2,
#     label="Deaths"
# )

# # Labels and Title
# plt.title("COVID-19 Analysis: Recovered vs Deaths")
# plt.xlabel("Country")
# plt.ylabel("Number of Cases")

# # Rotate country names
# plt.xticks(rotation=45)

# # Show legend
# plt.legend()

# # Adjust layout
# plt.tight_layout()

# # Display graph
# plt.show()
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