import pandas as pd

df = pd.read_csv("../data/final_jobs_skills.csv")

print("Rows & Columns:", df.shape)
print("Columns:", df.columns)
print("Skills Sample:", df['skills'].dropna().head())
print("Role Count:\n", df['role_category'].value_counts())