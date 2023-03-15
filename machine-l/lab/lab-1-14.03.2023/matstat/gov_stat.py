import pandas as pd
import matplotlib.pyplot as plt


def run():
    # Read Excel file
    df = pd.read_excel('./data/gov_data.xlsx')

    # Remove possible corrupted data
    df.dropna(inplace=True)

    # Drop old indexing
    df.drop(columns=df.columns[0], inplace=True)
    # Use year indexes
    df.set_index('Year', inplace=True)

    # Calculate and show statistics

    print("-----MEAN-----")
    print(df.mean())

    print("-----MODE-----")
    print(df.mode())

    print("-----VARIANCES-----")
    print(df.var())

    print("-----STD_DEVS-----")
    print(df.std())

    # Show histogram
    # df.hist(bins=10, figsize=(20, 10))
    plt.show()
