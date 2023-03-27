import pandas as pd
import seaborn as cbor
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv(
    'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/time-series/110/tavg/1/1/1895-2018.csv')

df.drop(df.columns[2], axis=1, inplace=True)
df.drop([0, 1, 2], inplace=True)
df = df.reset_index(drop=True)
df.columns = ['Date', 'Temperature']

df.iloc[:, 0] = df.iloc[:, 0].astype(int)
df.iloc[:, 1] = df.iloc[:, 1].astype(float)

df.Date = df.Date.floordiv(100)

print(df)

axes = cbor.regplot(x='Date', y='Temperature', data=df)
cbor.set_style("darkgrid")
axes.set_ylim(10, 70)
plt.show()

reg = linregress(df['Date'], df['Temperature'])

future_years = [2019, 2020, 2021, 2022]
future_temps = [reg.slope * year + reg.intercept for year in future_years]
for year, temp in zip(future_years, future_temps):
    print(f'The predicted average temperature for {year} is {temp:.2f}')

print("-----------------------")
past_years = [1850, 1860, 1870]
future_temps = [reg.slope * year + reg.intercept for year in past_years]
for year, temp in zip(past_years, future_temps):
    print(f'The predicted average temperature for {year} is {temp:.2f}')
