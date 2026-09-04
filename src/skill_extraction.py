import pandas as pd

skills_list = [
    "python","sql","excel","power bi","tableau",
    "machine learning","statistics","pandas","numpy",
    "java","spring","react","aws","docker",
    "kubernetes","html","css","javascript"
]
df = pd.read_csv("../data/final_jobs_cleaned.csv")

def extract_skills(text):
    text = str(text).lower()
    found = [skill for skill in skills_list if skill in text]
    return ",".join(found)

df['skills'] = df['description'].apply(extract_skills)

df.to_csv("../data/final_jobs_skills.csv", index=False)

print("Skill Extraction Done")