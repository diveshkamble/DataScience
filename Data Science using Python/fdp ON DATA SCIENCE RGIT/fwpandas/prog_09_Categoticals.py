import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3
"""
pandas can include categorical data in a DataFrame.
"""
#127
df = pd.DataFrame(
    {"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
#Convert the raw grades to a categorical data type.
df["grade"] = df["raw_grade"].astype("category")#128
print(' df["grade"] :\n',df["grade"])#129
print('-'*20)
#Rename the categories to more meaningful names
#(assigning to Series.cat.categories is inplace!).
df["grade"].cat.categories = ["very good", "good", "very bad"] #130
#Reorder the categories and simultaneously add the missing categories
#(methods under Series .cat return a new Series by default).
#131
df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"])
print('df["grade"] :\n',df["grade"] )#132
print('-'*20)
#Sorting is per order in the categories, not lexical order.
print(df.sort_values(by="grade"))#133
print('-'*20)
#Grouping by a categorical column also shows empty categories.
print(df.groupby("grade").size())#134

