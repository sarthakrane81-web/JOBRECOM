import pandas as pd
import matplotlib.pyplot as plt

# Load FINAL dataset
df = pd.read_csv("../data/final_jobs_skills.csv")

print(df.head())

# ⭐ Top Hiring Locations
plt.figure(figsize=(12,6))
df['location'].value_counts().head(10).plot(kind='bar')
plt.title("Top Hiring Locations")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("../reports/location_graph.png")
plt.close()

# ⭐ Top Companies
plt.figure(figsize=(12,6))
df['company'].value_counts().head(10).plot(kind='bar')
plt.title("Top Hiring Companies")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("../reports/company_graph.png")
plt.close()

# ⭐ Salary Distribution
plt.figure(figsize=(10,5))
df['salary_min'].dropna().plot(kind='hist', bins=20)
plt.title("Salary Distribution")
plt.tight_layout()
plt.savefig("../reports/salary_graph.png")
plt.close()

# ⭐ Skill Demand Analysis
skills_series = df['skills'].dropna().str.split(',')
skills_series = skills_series.explode()

plt.figure(figsize=(12,6))
skills_series.value_counts().head(10).plot(kind='bar')
plt.title("Most Demanded Skills")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("../reports/skills_graph.png")
plt.close()

print("All graphs saved inside reports folder ✅")