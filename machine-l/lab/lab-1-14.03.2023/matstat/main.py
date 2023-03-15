import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel('./assets/nkzp_Ukr 18-20ue.xlsx')

# Calculate and show statistics
print(df.describe)
print(df.columns)

df.hist(bins=10, figsize=(20, 10))
plt.show()
