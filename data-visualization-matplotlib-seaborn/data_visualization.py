# =====================================================
# PROJECT 02: DATA VISUALIZATION WITH MATPLOTLIB & SEABORN
# Dataset: Tips Dataset
# =====================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1. Load Dataset
tips = sns.load_dataset("tips")

# Create charts folder
os.makedirs("charts", exist_ok=True)

# 2. Dataset Inspection
print("\n--- First Five Rows ---")
print(tips.head())

print("\n--- Dataset Information ---")
tips.info()

print("\n--- Statistical Summary ---")
print(tips.describe())

print("\n--- Missing Values ---")
print(tips.isnull().sum())

# 3. Set Visualization Style
sns.set_theme(
    style="whitegrid",
    palette="deep",
    font_scale=1.1
)

# =====================================================
# CHART 1: HISTOGRAM
# Question: How are total bills distributed?
# =====================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=tips,
    x="total_bill",
    bins=20,
    kde=True,
    color="steelblue"
)

plt.title("Most Total Bills Fall Within a Moderate Range")
plt.xlabel("Total Bill (USD)")
plt.ylabel("Number of Meals")

plt.tight_layout()
plt.savefig("charts/histogram.png", dpi=150)
plt.show()

# =====================================================
# CHART 2: BOX PLOT
# Question: How do tips differ by day?
# =====================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=tips,
    x="day",
    y="tip",
    hue="day",
    palette="Set2",
    legend=False
)

plt.title("Tip Amounts Vary Across Different Days")
plt.xlabel("Day")
plt.ylabel("Tip Amount (USD)")

plt.tight_layout()
plt.savefig("charts/boxplot.png", dpi=150)
plt.show()

# =====================================================
# CHART 3: SCATTER PLOT
# Question: Does a larger bill mean a larger tip?
# =====================================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time",
    palette="Set2",
    s=70
)

plt.title("Larger Bills Tend to Have Larger Tips")
plt.xlabel("Total Bill (USD)")
plt.ylabel("Tip Amount (USD)")
plt.legend(title="Meal Time")

plt.tight_layout()
plt.savefig("charts/scatterplot.png", dpi=150)
plt.show()

# =====================================================
# CHART 4: CORRELATION HEATMAP
# Question: Which numerical variables move together?
# =====================================================

correlation = tips.select_dtypes(
    include="number"
).corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Between Numerical Variables")

plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png", dpi=150)
plt.show()

# =====================================================
# CHART 5: BAR CHART
# Average Tip by Day
# =====================================================

plt.figure(figsize=(8, 5))

sns.barplot(
    data=tips,
    x="day",
    y="tip",
    hue="day",
    estimator="mean",
    errorbar=None,
    palette="viridis",
    legend=False
)

plt.title("Average Tip Amount by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip (USD)")

plt.tight_layout()
plt.savefig("charts/bar_chart.png", dpi=150)
plt.show()

# =====================================================
# CHART 6: COMPLETE DASHBOARD
# =====================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.histplot(
    data=tips,
    x="total_bill",
    bins=20,
    color="steelblue",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Distribution of Total Bills")
axes[0, 0].set_xlabel("Total Bill (USD)")

sns.boxplot(
    data=tips,
    x="day",
    y="tip",
    hue="day",
    palette="Set2",
    legend=False,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Tip Distribution by Day")
axes[0, 1].set_xlabel("Day")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time",
    palette="Set2",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Total Bill vs Tip")
axes[1, 0].set_xlabel("Total Bill (USD)")

sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues",
    fmt=".2f",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Correlation Heatmap")

plt.suptitle(
    "Tips Dataset - Data Visualization Dashboard",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()
plt.savefig("charts/tips_dashboard.png", dpi=150)
plt.show()

# =====================================================
# FINAL STATISTICAL INSIGHTS
# =====================================================

print("\n========== PROJECT FINDINGS ==========")

print("\n1. Average Total Bill:")
print(round(tips["total_bill"].mean(), 2), "USD")

print("\n2. Average Tip:")
print(round(tips["tip"].mean(), 2), "USD")

print("\n3. Correlation Between Total Bill and Tip:")
print(round(
    tips["total_bill"].corr(tips["tip"]), 2
))

print("\n4. Average Tip by Day:")
print(tips.groupby("day", observed=True)["tip"].mean().round(2))

print("\n5. Average Bill by Meal Time:")
print(tips.groupby("time", observed=True)["total_bill"].mean().round(2))

print("\nAll charts saved successfully in the charts folder!")
print("Data Visualization Project Completed!")