import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("../data/final_jobs_skills.csv")

df = df.dropna(subset=['salary_min','salary_max'])

X = df[['salary_min']]
y = df['salary_max']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)

print("Model Accuracy:", score)