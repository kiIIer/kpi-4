import pandas as pd
import matplotlib.pyplot as plt

scv_url = 'https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv'

df = pd.read_csv(scv_url)

pd.set_option('precision', 2)

# View part of dataset
print(df.head())
print(df.tail())
