'''pandas is a software library written for python programming language
for data manipulation and analysis.pandas build on top of
numpy,scipyand matplotlib'''
#pandas well suited for different types of data
#tabular data with heterogenously-typed columns
#ordered and unordered time series data
#arbitary matrix data with row and column lab
'''any other form of observational/statistical data sets. the data actually need not be
labelled at all to be placed into a pandas data structure'''
#matplotlib is data visulaization module
#numpy is fundamental package for comuting scientific calculations in python, n dimensional array

'''scipy is module for scientific calculations like otimization,
linear algebra, integration'''

import pandas as pd

xyz_web={'Day':[1,2,3,4,5,6],"visitors":[1000,700,6000,1000,400,350],
         'Bounce_rate':[20,20,23,15,10,34]}
type(xyz_web)
df=pd.DataFrame(xyz_web)
print(df)

'''slicing data frame, changing the index, data conversion, joining and merging, concatenation,
changing column names'''

#slicing
print(df.head(2))
print(df.tail(2))

#merging
df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_gdp":[50,45,45,67]},
index=[2001,2002,2003,2004])

df2=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_gdp":[50,45,45,67]},
index=[2005,2006,2007,2008])

merge= pd.merge(df1,df2)
print(merge)


#merging on specific column
df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_gdp":[50,45,45,67]},
index=[2001,2002,2003,2004])
print(df1)

df2=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_gdp":[50,45,45,67]},
index=[2005,2006,2007,2008])
print(df2)

merge= pd.merge(df1,df2,on="HPI")
print(merge)


#joining two data frames
df1=pd.DataFrame({"Int_rate":[2,1,2,3],"IND_gdp":[50,45,45,67]},
index=[2001,2002,2003,2004])
print(df1)


df2=pd.DataFrame({"Low_tier_HPI":[50,45,67,34],"unemployment":[1,3,5,6]},
                    index=[2001,2003,2004,2004])

joined=df1.join(df2)

print(joined)

#chaning index and column names
df=pd.DataFrame({"day":[1,2,3,4],"visitors":[200,100,230,300],"Bounce_rate":[20,45,60,10]})

print(df)

df.set_index("day")
df.set_index("day",inplace=True)
print(df)

#ploting to visulaize data

import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

df=pd.DataFrame({"day":[1,2,3,4],"visitors":[200,100,230,300],"Bounce_rate":[20,45,60,10]})

df.set_index("day",inplace=True)

df.plot()
plt.show()


#chaning column header to users
df=pd.DataFrame({"day":[1,2,3,4],"visitors":[200,100,230,300],"Bounce_rate":[20,45,60,10]})
df=df.rename(columns={"visitors":"users"})

print(df)

#concatenation of data(row) in data frame
df1=pd.DataFrame({'HPI':[80,85,88,85],'int_rate':[2,3,2,2],
                  "US_GDP_thousand":[50,55,65,55]},
                 index=[2001,2002,2003,2004])
print(df1)

df2=pd.DataFrame({'HPI':[80,85,88,85],'int_rate':[2,3,2,2],
                  "US_GDP_thousand":[50,55,65,55]},
                 index=[2005,2006,2007,2008])
print(df2)

Concat=pd.concat([df1,df2])
print(Concat)


#data munging means converting one format of data to other format
#csv to html, xml to json

'''country=pd.read_csv("C:\\\\path of csv file",index_col=0)

country.to_html('edu.html')'''



#python for statistics
#mean,median,mode,variance

from statistics import mean

print(mean([1,3,4,6,7,8,9,10]))


from statistics import median

print(median([1,3,4,6,7,8,9,10]))

from statistics import variance

print(variance([1,3,4,6,7,8,9,10]))



#

































