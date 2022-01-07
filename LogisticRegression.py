import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("insurance_data.csv")
print(df.head())
print(df.shape)
plt.xlabel('age')
plt.ylabel('bought insurance')
plt.grid()
plt.scatter(df.age, df.bought_insurance, marker='*', color='red')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance, test_size=0.3)
print(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
print(y_predict)
print(y_test)
print(model.predict_proba(X_test))
print(model.score(X_test, y_test))