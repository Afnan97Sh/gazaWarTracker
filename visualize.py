import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read Excel file

df = pd.read_excel("data/Book1.xlsx")

# Convert date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Line Chart – Martyr count by date
plt.figure(figsize=(10, 6))
sns.lineplot(x="Date", y="Martyr Count", data=df, marker="o")
plt.title("Martyrs by Date")
plt.xlabel("Date")
plt.ylabel("Martyr Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Chart – Most damaged regions
region_damage = df.groupby("Region")["Damaged Homes Count"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=region_damage.values, y=region_damage.index)
plt.title("Most Damaged Regions")
plt.xlabel("Number of Damaged Homes")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

# Pie Chart  Attack type distribution
attack_distribution = df["Attack Type"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(attack_distribution, labels=attack_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title("Attack Type Distribution")
plt.tight_layout()
plt.show()
#Bar chart of days with the highest martyr counts.
top_days = df.sort_values("Martyr Count", ascending=False).head(5)
plt.figure(figsize=(8, 6))
sns.barplot(x=top_days["Date"].dt.strftime('%Y-%m-%d'), y=top_days["Martyr Count"])
plt.title("Top 5 Deadliest Days")
plt.xlabel("Date")
plt.ylabel("Martyr Count")
plt.tight_layout()
plt.show()

# Heatmap of Damaged Homes by Region and Attack Type
pivot_table = df.pivot_table(
    index="Region", columns="Attack Type", values="Damaged Homes Count", aggfunc="sum", fill_value=0
)

plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="Reds")
plt.title("Damaged Homes by Region and Attack Type")
plt.tight_layout()
plt.show()
