import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
df=pd.read_csv("Netflix/Netflix Dataset.csv")
print(df)

def replace_unknown(x):
    x = str(x).strip()

    # Percentage
    if re.fullmatch(r'\d+%', x):
        return "Unknown"

    # Time (HH:MM)
    if re.fullmatch(r'\d{1,2}:\d{2}', x):
        return "Unknown"

    # Number (comma allowed)
    if re.fullmatch(r'[\d,]+', x):
        return "Unknown"

    # Dates like Oct-01, Feb-09, 22-Jul
    if re.fullmatch(r'[A-Za-z]{3}-\d{2}', x) or re.fullmatch(r'\d{2}-[A-Za-z]{3}', x):
        return "Unknown"

    return x

df["Title"] = df["Title"].apply(replace_unknown)
#shows a raw data
print(df)
#drop duplicates values
df=df.drop_duplicates()
print(df)
#fill na
df=df.bfill()
print(df)
#check any columns contain null values
print(df.isnull().sum())
#there is duplicate value occur in cast column soo!! fillna should used
df["Cast"] = df["Cast"].fillna("Demián Bichir")
print(df.isnull().sum())
df.to_csv("Netflix_clean_data_file.csv",index=False)