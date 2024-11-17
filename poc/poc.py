import pandas as pd

df = pd.read_excel(r"E:\data\test.xlsx", header=0)
print(df)

print("------------------------------------------------------------------------------------")
#  求总分最高的三个学生的名字和总分数
df1 = df.groupby("name")["record"].sum().reset_index().sort_values(by='record', ascending=False).head(3).reset_index()[["name", "record"]]
print(df1)
print("------------------------------------------------------------------------------------")
# 查成绩，求最高分
high_score = df["record"].max()
df2 = df[df["record"] == high_score]
print(df2)
print("------------------------------------------------------------------------------------")
# 查成绩，求平均值
df3 = df.groupby("name")["record"].mean().reset_index().sort_values(by='record', ascending=False).reset_index()[["name", "record"]]
print(df3)
