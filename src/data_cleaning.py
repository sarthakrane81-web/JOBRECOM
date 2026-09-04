import pandas as pd

df = pd.read_csv("../data/final_jobs.csv")

print("Before Cleaning:", len(df))

# remove duplicates
df.drop_duplicates(inplace=True)

# convert salary columns to numeric
df['salary_min'] = pd.to_numeric(df['salary_min'], errors='coerce')
df['salary_max'] = pd.to_numeric(df['salary_max'], errors='coerce')

# remove rows without title
df.dropna(subset=['title'], inplace=True)

# fill missing company/location
df['company'].fillna("Unknown", inplace=True)
df['location'].fillna("India", inplace=True)

df.to_csv("../data/final_jobs_cleaned.csv", index=False)

print("After Cleaning:", len(df))