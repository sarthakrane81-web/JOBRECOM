import requests
import pandas as pd

app_id = "b2334e69"
app_key = "3cee26c9aaa13c230964a254d492e518"

roles = [
    "data analyst",
    "software developer",
    "java developer",
    "machine learning engineer"
]
 
all_jobs = []

for role in roles:
    for page in range(1, 15):

        url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}?app_id={app_id}&app_key={app_key}&what={role}"

        res = requests.get(url)
        data = res.json()

        for job in data.get('results', []):

            all_jobs.append({
                "title": job.get('title'),
                "company": job.get('company', {}).get('display_name'),
                "location": job.get('location', {}).get('display_name'),
                "salary_min": job.get('salary_min'),
                "salary_max": job.get('salary_max'),
                "description": job.get('description'),
                "role_category": role
            })

df = pd.DataFrame(all_jobs)

df.to_csv("../data/multi_role_jobs.csv", index=False)

print("Total Jobs:", len(df))
