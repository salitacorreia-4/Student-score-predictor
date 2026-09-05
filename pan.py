import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

# Drop or fill missing values
df = df.dropna()