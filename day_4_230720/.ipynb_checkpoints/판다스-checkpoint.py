import pandas as pd
import seaborn as sns
import pprint as pp

class pds:
    def pd1(self):
        df = pd.read_csv("C:/Users/koll2/OneDrive/2023_summer_program/code/성적처리/sungjuk2.csv", encoding="UTF-8")
        return df

    def pd2(self):
        df = sns.load_dataset("titanic")
        return df

    def pd3(self):
        df = self.pd1()
        print(df[["국어","수학","영어"]])

    def pd4(self):
        df = self.pd2()
        print(df[["age","fare"]])

    def pd5(self):
        df = self.pd1()
        return df.loc[0:9:2]

    def pd6(self):
        df = self.pd1()
        return df.loc[0:9:2, ["이름","국어","영어"]]
    
a = pds()

# print(a.pd1())
# print(a.pd2())
pp.pprint(a.pd6())
# a.pd4()