import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv('homeprice.csv')
print(df)

plt.xlabel('area')
plt.ylabel('price')
plt.grid()
plt.scatter(df.area, df.price, color='blue', marker='*')
plt.show()

new_df = df.drop('price', axis="columns")
print(new_df)

price = df.price
print(type(price))
np.array(price)

reg = linear_model.LinearRegression()
reg.fit(new_df, price)
print(reg.predict([[4500]]))
print(reg.coef_)
print(reg.intercept_)

area_df = pd.read_csv('area.csv')
area_df.head()

p = reg.predict(area_df)
print(p)
area_df['predicted_prices'] = p
print(area_df)

area_df.to_csv('prediction.csv')

