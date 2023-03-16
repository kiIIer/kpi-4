import pandas as pd
import matplotlib.pyplot as plt


def run():
    scv_url = 'https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv'

    df = pd.read_csv(scv_url)

    pd.set_option('precision', 2)

    # View part of dataset
    print(df.head())
    print(df.tail())

    # Rename column
    print(df.columns)
    df.rename(columns={df.columns[-1]: 'class'}, inplace=True)
    print(df.columns)

    # Simple data analytics

    # Min
    min_row = df.loc[df['age'].idxmin()]
    print("-----Youngest person-----")
    print(min_row)

    # Max
    max_row = df.loc[df['age'].idxmax()]
    print("-----Oldest person-----")
    print(max_row)

    # Average
    average_age = df.T.loc['age'].mean()
    print("-----Average Age-----")
    print(average_age)

    # Stuff with women

    # first class women
    women_in_first_class = df[(df['sex'] == 'female') & (df['class'] == '1st')]
    print("-----First class girls-----")
    print(women_in_first_class)

    # Youngest girl
    youngest_woman = women_in_first_class['age'].min()
    print("-----Fbi plz don't open up i didn't know her age-----")
    print(youngest_woman)

    # More mature girl
    oldest_woman = women_in_first_class['age'].max()
    print("-----Mature woman-----")
    print(oldest_woman)

    # How many are still alive
    survived_count = women_in_first_class['survived'].replace({'yes': 1, 'no': 0}).sum()
    print("-----How many survived-----")
    print(survived_count)

    # drawing histogram of age
    plt.hist(df['age'], bins=50)

    # Let's add some labels, so it'll be a bit easier to read
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')

    plt.show()
