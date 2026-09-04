import requests
import pandas as pd

app_id = "b2334e69"
app_key = "3cee26c9aaa13c230964a254d492e518"

all_jobs = []

for page in range(1, 10):   # change 10 → more pages
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}?app_id={app_id}&app_key={app_key}&what=data%20analyst"

    response = requests.get(url)
    data = response.json()

    for job in data['results']:
        all_jobs.append({
            "Title": job['title'],
            "Company": job['company']['display_name'],
            "Location": job['location']['display_name'],
            "Salary_Min": job.get('salary_min'),
            "Salary_Max": job.get('salary_max')
        })

df = pd.DataFrame(all_jobs)
df.to_csv("jobs_data_big.csv", index=False)

print("Total Jobs Collected:", len(df))