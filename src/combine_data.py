import pandas as pd
import os

# ⭐ Read new data sources
df_api = pd.read_csv("../data/adzuna_jobs.csv")
df_kaggle = pd.read_csv("../data/IndianCompanies.csv")
df_multi = pd.read_csv("../data/multi_role_jobs.csv")

# ⭐ Combine new data
new_df = pd.concat([df_api, df_kaggle, df_multi], ignore_index=True)

file_path = "../data/final_jobs.csv"

# ⭐ Append if file already exists
if os.path.exists(file_path):
    old_df = pd.read_csv(file_path)
    final_df = pd.concat([old_df, new_df], ignore_index=True)
else:
    final_df = new_df

# ⭐ Save dataset
final_df.to_csv(file_path, index=False)

print("Dataset updated successfully. Total rows:", len(final_df))