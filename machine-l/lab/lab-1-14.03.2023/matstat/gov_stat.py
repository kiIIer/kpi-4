import pandas as pd
import matplotlib.pyplot as plt


def run():
    # Read Excel file
    df = pd.read_excel('./data/gov_data.xlsx')

    # Calculate and show statistics
    print(df.mean())

    # Show histogram
    df.hist(bins=10, figsize=(20, 10))
    plt.show()
