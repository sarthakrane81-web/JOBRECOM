import requests
import pandas as pd
import datetime

app_id = "b2334e69"
app_key = "3cee26c9aaa13c230964a254d492e518"

all_jobs = []

for page in range(1, 25):

    url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}?app_id={app_id}&app_key={app_key}&what=data%20analyst"

    response = requests.get(url)
    data = response.json()

    for job in data.get('results', []):

        title = job.get('title')

        company = job.get('company', {}).get('display_name')

        location = job.get('location', {}).get('display_name')

        salary_min = job.get('salary_min')
        salary_max = job.get('salary_max')

        description = job.get('description')

        all_jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "salary_min": salary_min,
            "salary_max": salary_max,
            "description": description,
            "date_collected": datetime.date.today()
        })

df = pd.DataFrame(all_jobs)

df.to_csv("../data/adzuna_jobs.csv", index=False)

print("Total API Jobs Collected:", len(df))