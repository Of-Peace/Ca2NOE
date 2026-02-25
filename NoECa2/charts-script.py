import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("amazon_cleaned_rows_1_to_799.xlsx")

# Keep first 100 rows
df_100 = df.head(100)
df_100.to_csv("amazon_100_rows.csv", index=False)

# Convert numeric columns if needed
df_100["price"] = pd.to_numeric(df_100["price"], errors="coerce")
df_100["number_of_reviews"] = pd.to_numeric(df_100["number_of_reviews"], errors="coerce")

# -----------------------------
# Descriptive Statistics
# -----------------------------
desc_stats = df_100.describe().T
desc_stats["median"] = df_100.median(numeric_only=True)
desc_stats["mode"] = df_100.mode(numeric_only=True).iloc[0]

desc_stats = desc_stats[["mean", "50%", "mode", "min", "max", "std"]]
desc_stats.rename(columns={"50%": "median", "std": "standard_deviation"}, inplace=True)

desc_stats.to_csv("descriptive_statistics.csv")

# -----------------------------
# Missing Values
# -----------------------------
missing_counts = df_100.isnull().sum()
missing_counts.to_csv("missing_value_counts.csv")

# -----------------------------
# 1. Improved Bar Chart
# -----------------------------
numeric_cols = df_100.select_dtypes(include="number").columns

plt.figure()
df_100[numeric_cols].mean().plot(
    kind="bar",
    color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
)
plt.title("Improved Bar Chart: Average of Numerical Variables")
plt.xlabel("Variables")
plt.ylabel("Average Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("improved_bar_chart.png")
plt.close()

# -----------------------------
# 2. Dot Chart – Number of Reviews
# -----------------------------
plt.figure()
plt.scatter(
    range(len(df_100["number_of_reviews"])),
    df_100["number_of_reviews"],
    color="#d62728"
)
plt.title("Dot Chart of Number of Reviews")
plt.xlabel("Row Index")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("dot_chart_reviews.png")
plt.close()

# -----------------------------
# 3. Line Chart – Number of Reviews
# -----------------------------
plt.figure()
plt.plot(
    df_100["number_of_reviews"],
    color="#1f77b4"
)
plt.title("Line Chart: Trend of Number of Reviews")
plt.xlabel("Row Index")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()