import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns

df = pd.read_csv(
    'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/time-series/110/tavg/1/1/1895-2018.csv')

df.drop(df.columns[2], axis=1, inplace=True)
df.drop([0, 1, 2], inplace=True)
df = df.reset_index(drop=True)
df.columns = ['Date', 'Temperature']

df[df.columns[0]] = df[df.columns[0]].astype(int)
df[df.columns[1]] = df[df.columns[1]].astype(float)

df.Date = df.Date.floordiv(100)

print(df)

X_train, X_test, y_train, y_test = train_test_split(df.Date.values.reshape(-1, 1), df.Temperature.values, test_size=0.2,
                                                    random_state=42)

print(X_train.shape)
print(y_train.shape)

linear_regression = LinearRegression()

linear_regression.fit(X_train, y_train)

print(linear_regression.coef_)
print(linear_regression.intercept_)

predicted = linear_regression.predict(X_test)

expected = y_test

for p, e in zip(predicted[::5], expected[::5]):
    print(f'predicted: {p:.2f}, expected: {e:.2f}')

predict = (lambda x: linear_regression.coef_ * x + linear_regression.intercept_)

print(predict(2019))
print(predict(1890))

axes = sns.scatterplot(data=df, x='Date', y='Temperature', hue='Temperature', palette='winter', legend=False)
axes.set_ylim(10, 70)

x = np.array([min(df.Date.values), max(df.Date.values)])
y = predict(x)

line = plt.plot(x, y)

plt.show()
