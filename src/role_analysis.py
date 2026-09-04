import pandas as pd
import matplotlib.pyplot as plt

# ⭐ Load FINAL dataset
df = pd.read_csv("../data/final_jobs_skills.csv")

# ⭐ Graph 1 — Jobs by Role
plt.figure(figsize=(12,6))
df['role_category'].value_counts().plot(kind='bar')
plt.title("Jobs by Role Category")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("../reports/role_jobs.png")
plt.close()

# ⭐ Graph 2 — Average Salary by Role
plt.figure(figsize=(12,6))
df['salary_min'].fillna(df['salary_min'].median(), inplace=True)

df.groupby('role_category')['salary_min'].mean().plot(kind='bar')
plt.title("Average Salary by Role")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("../reports/role_salary.png")
plt.close()

# ⭐ Graph 3 — Skill Count by Role
plt.figure(figsize=(12,6))
df.groupby('role_category')['skills'].count().plot(kind='bar')
plt.title("Skill Demand by Role")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("../reports/role_skills.png")
plt.close()

print("Role analysis graphs saved successfully ✅")