import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("../reports", exist_ok=True)

df = pd.read_csv("../data/final_jobs_skills.csv")

# convert date column
df['date_collected'] = pd.to_datetime(df['date_collected'])

# ⭐ Daily Job Count Trend
trend = df.groupby('date_collected').size()

plt.figure(figsize=(12,6))
trend.plot(kind='line', marker='o')
plt.title("Daily Job Collection Trend")
plt.xlabel("Date")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("../reports/daily_trend.png")
plt.close()

print("Daily trend graph saved ✅")