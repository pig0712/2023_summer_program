# 송교수님 사이트
# http://jjmoak.iwinv.net/wp/?page_id=16241

import pandas as pd
import os

os.system("cls")

df = pd.read_csv("C:/Users/koll2/OneDrive/2023_summer_program/day_5_230712/data.csv")

# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.describe())
# print(df.info())
# print(df.count())
# print(df["avgTa"].count())
# print(df[["avgTa" , "minTa" , "maxTa"]].count())
# print(df["maxTa"].value_counts())

# print(df.mean())
# print(df["maxTa"].mean())
# print(df["maxTa"].max())

# print(df[["avgTa" , "minTa" , "maxTa"]].max())
# print(df[["avgTa" , "minTa" , "maxTa"]].min())
# df["avgTa"].plot()

# df2 = df[df["tm"].str[:4]=="2000"]
# df2["avgTa"].plot()
df[df["tm"].str[:4]=="2000"]["avgTa"].plot()