Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============
Traceback (most recent call last):
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 166, in to_rgba
    rgba = _colors_full_map.cache[c, alpha]
KeyError: ('grid', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/RGIT/Desktop/mohd/02/piechart01.py", line 10, in <module>
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.2f%',shadow=True,startangle=140)# 1.1f%%
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\pyplot.py", line 3338, in pie
    frame=frame, rotatelabels=rotatelabels, data=data)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1855, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 2902, in pie
    **wedgeprops)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 1065, in __init__
    Patch.__init__(self, **kwargs)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 88, in __init__
    self.set_facecolor(facecolor)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 315, in set_facecolor
    self._set_facecolor(color)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 305, in _set_facecolor
    self._facecolor = colors.to_rgba(color, alpha)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 168, in to_rgba
    rgba = _to_rgba_no_colorcycle(c, alpha)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 212, in _to_rgba_no_colorcycle
    raise ValueError("Invalid RGBA argument: {!r}".format(orig_c))
ValueError: Invalid RGBA argument: 'grid'
>>> 
============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============
Traceback (most recent call last):
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 166, in to_rgba
    rgba = _colors_full_map.cache[c, alpha]
KeyError: ('grid', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/RGIT/Desktop/mohd/02/piechart01.py", line 10, in <module>
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.2f%',shadow=True,startangle=140)# 1.1f%%
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\pyplot.py", line 3338, in pie
    frame=frame, rotatelabels=rotatelabels, data=data)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1855, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 2902, in pie
    **wedgeprops)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 1065, in __init__
    Patch.__init__(self, **kwargs)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 88, in __init__
    self.set_facecolor(facecolor)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 315, in set_facecolor
    self._set_facecolor(color)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 305, in _set_facecolor
    self._facecolor = colors.to_rgba(color, alpha)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 168, in to_rgba
    rgba = _to_rgba_no_colorcycle(c, alpha)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 212, in _to_rgba_no_colorcycle
    raise ValueError("Invalid RGBA argument: {!r}".format(orig_c))
ValueError: Invalid RGBA argument: 'grid'
>>> 
============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============
Traceback (most recent call last):
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 166, in to_rgba
    rgba = _colors_full_map.cache[c, alpha]
KeyError: ('grid', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/RGIT/Desktop/mohd/02/piechart01.py", line 10, in <module>
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.2f%',shadow=True,startangle=140)# 1.1f%%
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\pyplot.py", line 3338, in pie
    frame=frame, rotatelabels=rotatelabels, data=data)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1855, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 2902, in pie
    **wedgeprops)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 1065, in __init__
    Patch.__init__(self, **kwargs)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 88, in __init__
    self.set_facecolor(facecolor)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 315, in set_facecolor
    self._set_facecolor(color)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 305, in _set_facecolor
    self._facecolor = colors.to_rgba(color, alpha)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 168, in to_rgba
    rgba = _to_rgba_no_colorcycle(c, alpha)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 212, in _to_rgba_no_colorcycle
    raise ValueError("Invalid RGBA argument: {!r}".format(orig_c))
ValueError: Invalid RGBA argument: 'grid'
>>> 
=============================== RESTART: Shell ===============================
>>> 
============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============
Traceback (most recent call last):
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 166, in to_rgba
    rgba = _colors_full_map.cache[c, alpha]
KeyError: ('grid', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/RGIT/Desktop/mohd/02/piechart01.py", line 10, in <module>
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.2f%',shadow=True,startangle=140)# 1.1f%%
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\pyplot.py", line 3338, in pie
    frame=frame, rotatelabels=rotatelabels, data=data)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1855, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 2902, in pie
    **wedgeprops)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 1065, in __init__
    Patch.__init__(self, **kwargs)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 88, in __init__
    self.set_facecolor(facecolor)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 315, in set_facecolor
    self._set_facecolor(color)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\patches.py", line 305, in _set_facecolor
    self._facecolor = colors.to_rgba(color, alpha)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 168, in to_rgba
    rgba = _to_rgba_no_colorcycle(c, alpha)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\colors.py", line 212, in _to_rgba_no_colorcycle
    raise ValueError("Invalid RGBA argument: {!r}".format(orig_c))
ValueError: Invalid RGBA argument: 'grid'
>>> 
============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============
Traceback (most recent call last):
  File "C:/Users/RGIT/Desktop/mohd/02/piechart01.py", line 10, in <module>
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.2f%',shadow=True,startangle=140)# 1.1f%%
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\pyplot.py", line 3338, in pie
    frame=frame, rotatelabels=rotatelabels, data=data)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1855, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 2938, in pie
    s = autopct % (100. * frac)
ValueError: incomplete format
>>> 
============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============

============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============
>>> 
============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============

============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============

============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============

============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============

============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============
>>> 
============ RESTART: C:/Users/RGIT/Desktop/mohd/02/piechart01.py ============
>>> 
========== RESTART: C:/Users/RGIT/Desktop/mohd/02/scatterplot01.py ==========

========== RESTART: C:/Users/RGIT/Desktop/mohd/02/scatterplot01.py ==========

========== RESTART: C:/Users/RGIT/Desktop/mohd/02/scatterplot01.py ==========

========== RESTART: C:/Users/RGIT/Desktop/mohd/02/scatterplot01.py ==========

========== RESTART: C:/Users/RGIT/Desktop/mohd/02/scatterplot01.py ==========

========== RESTART: C:/Users/RGIT/Desktop/mohd/02/scatterplot01.py ==========

========== RESTART: C:/Users/RGIT/Desktop/mohd/02/scatterplot01.py ==========
>>> 
============= RESTART: C:/Users/RGIT/Desktop/mohd/02/panda01.py =============
Traceback (most recent call last):
  File "C:/Users/RGIT/Desktop/mohd/02/panda01.py", line 3, in <module>
    import matplot.pyplot as plt#3
ModuleNotFoundError: No module named 'matplot'
>>> 
============= RESTART: C:/Users/RGIT/Desktop/mohd/02/panda01.py =============
Traceback (most recent call last):
  File "C:/Users/RGIT/Desktop/mohd/02/panda01.py", line 5, in <module>
    s=pd.Series(np.random.randint(0,7,size=10))#68
NameError: name 'np' is not defined
>>> 
============= RESTART: C:/Users/RGIT/Desktop/mohd/02/panda01.py =============
Traceback (most recent call last):
  File "C:/Users/RGIT/Desktop/mohd/02/panda01.py", line 5, in <module>
    s=pd.Series(np.random.randint(0,7,size=10))#68
AttributeError: module 'pandas' has no attribute 'random'
>>> 
============= RESTART: C:/Users/RGIT/Desktop/mohd/02/panda01.py =============
0    1
1    1
2    3
3    0
4    5
5    1
6    2
7    6
8    1
9    4
dtype: int32
--------------------
1    4
6    1
5    1
4    1
3    1
2    1
0    1
dtype: int64
>>> import pandas as pd
>>> s=pd.Series)[1,3,5,np.nan,6,8])
SyntaxError: invalid syntax
>>> s=pd.Series[1,3,5,np.nan,6,8])
SyntaxError: invalid syntax
>>> 
>>> s=pd.Series([1,3,5,np.nan,6,8])
>>> print(s)
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> dates=pd.date_range('20130101',periods=6)
>>> print(dates)
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> dates=pd.date_range('20180103',periods=5)
>>> print(dates)
DatetimeIndex(['2018-01-03', '2018-01-04', '2018-01-05', '2018-01-06',
               '2018-01-07'],
              dtype='datetime64[ns]', freq='D')
>>> import pandas as pd
>>> import numpy as np
>>> s=pd.Series([1,3,5,np.nan,6,8])
>>> print(s)
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> dates=pd.date_range('20180103',periods=5)
>>> print(dates)
DatetimeIndex(['2018-01-03', '2018-01-04', '2018-01-05', '2018-01-06',
               '2018-01-07'],
              dtype='datetime64[ns]', freq='D')
>>> df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
Traceback (most recent call last):
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4859, in create_block_manager_from_blocks
    mgr = BlockManager(blocks, axes)
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 3282, in __init__
    self._verify_integrity()
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 3493, in _verify_integrity
    construction_error(tot_items, block.shape[1:], self.axes)
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4843, in construction_error
    passed, implied))
ValueError: Shape of passed values is (4, 6), indices imply (4, 5)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 379, in __init__
    copy=copy)
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 536, in _init_ndarray
    return create_block_manager_from_blocks([values], [columns, index])
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4866, in create_block_manager_from_blocks
    construction_error(tot_items, blocks[0].shape[1:], axes, e)
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4843, in construction_error
    passed, implied))
ValueError: Shape of passed values is (4, 6), indices imply (4, 5)
>>> df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
Traceback (most recent call last):
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4859, in create_block_manager_from_blocks
    mgr = BlockManager(blocks, axes)
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 3282, in __init__
    self._verify_integrity()
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 3493, in _verify_integrity
    construction_error(tot_items, block.shape[1:], self.axes)
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4843, in construction_error
    passed, implied))
ValueError: Shape of passed values is (4, 6), indices imply (4, 5)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 379, in __init__
    copy=copy)
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 536, in _init_ndarray
    return create_block_manager_from_blocks([values], [columns, index])
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4866, in create_block_manager_from_blocks
    construction_error(tot_items, blocks[0].shape[1:], axes, e)
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4843, in construction_error
    passed, implied))
ValueError: Shape of passed values is (4, 6), indices imply (4, 5)
>>> df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))dates=pd.date_range('20180103',periods=6)
SyntaxError: invalid syntax
>>> dates=pd.date_range('20180103',periods=6)
>>> df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
>>> print (df)
                   A         B         C         D
2018-01-03  2.260439  1.597635 -0.124683  0.128566
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
2018-01-05 -0.753962  1.028336 -0.115419 -1.413627
2018-01-06 -0.527723  0.401749  0.505246 -1.706658
2018-01-07  0.675116 -0.423552  0.662218 -0.220922
2018-01-08  1.774308  0.568452 -0.775076  1.302595
>>> df2=pd.DataFrame({'A':1.,
		      'B':pd.Timestamp('20130102'),
		      'C':pd.Series(1,index=list(range(4)),dtype'float32')
		      
SyntaxError: invalid syntax
>>> df2=pd.DataFrame({'A':1.,
		      'B':pd.Timestamp('20130102'),
		      'C':pd.Series(1,index=list(range(4)),dtype='float32'),
		      'D':np.array([3]*4),dtype='int32'),
		     
SyntaxError: invalid syntax
>>> df2=pd.DataFrame({'A':1.,
		      'B':pd.Timestamp('20130102'),
		      'C':pd.Series(1,index=list(range(4)),dtype='float32'),
		      'D':np.array([3]*4,dtype='int32'),
		      'E':pd.categorial(["test","train","test","train"])
		      'F':'foo'
		      
SyntaxError: invalid syntax
>>> df2=pd.DataFrame({'A':1.,
		      'B':pd.Timestamp('20130102'),
		      'C':pd.Series(1,index=list(range(4)),dtype='float32'),
		      'D':np.array([3]*4,dtype='int32'),
		      'E':pd.categorial(["test","train","test","train"])
		      'F':'foo'})
		      
SyntaxError: invalid syntax
>>> df2=pd.DataFrame({'A':1.,
		      'B':pd.Timestamp('20130102'),
		      'C':pd.Series(1,index=list(range(4)),dtype='float32'),
		      'D':np.array([3]*4,dtype='int32'),
		      'E':pd.categorial(["test","train","test","train"]),
		      'F':'foo'})
		      
Traceback (most recent call last):
  File "<pyshell#31>", line 5, in <module>
    'E':pd.categorial(["test","train","test","train"]),
AttributeError: module 'pandas' has no attribute 'categorial'
>>> df2=pd.DataFrame({'A':1.,
		      'B':pd.Timestamp('20130102'),
		      'C':pd.Series(1,index=list(range(4)),dtype='float32'),
		      'D':np.array([3]*4,dtype='int32'),
		      'E':pd.Categorical(["test","train","test","train"]),
		      'F':'foo'})
		      
>>> print(df2)
		      
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df2.dates
		      
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    df2.dates
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'dates'
>>> df2.dtypes
		      
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
>>> print("df.head():\n",df.head())
		      
df.head():
                    A         B         C         D
2018-01-03  2.260439  1.597635 -0.124683  0.128566
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
2018-01-05 -0.753962  1.028336 -0.115419 -1.413627
2018-01-06 -0.527723  0.401749  0.505246 -1.706658
2018-01-07  0.675116 -0.423552  0.662218 -0.220922
>>> print("df.head():\n",df.head(2))
		      
df.head():
                    A         B         C         D
2018-01-03  2.260439  1.597635 -0.124683  0.128566
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
>>> df
		      
                   A         B         C         D
2018-01-03  2.260439  1.597635 -0.124683  0.128566
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
2018-01-05 -0.753962  1.028336 -0.115419 -1.413627
2018-01-06 -0.527723  0.401749  0.505246 -1.706658
2018-01-07  0.675116 -0.423552  0.662218 -0.220922
2018-01-08  1.774308  0.568452 -0.775076  1.302595
>>> df.tail(3)
		      
                   A         B         C         D
2018-01-06 -0.527723  0.401749  0.505246 -1.706658
2018-01-07  0.675116 -0.423552  0.662218 -0.220922
2018-01-08  1.774308  0.568452 -0.775076  1.302595
>>> df.idex
		      
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    df.idex
  File "C:\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'idex'
>>> df.index
		      
DatetimeIndex(['2018-01-03', '2018-01-04', '2018-01-05', '2018-01-06',
               '2018-01-07', '2018-01-08'],
              dtype='datetime64[ns]', freq='D')
>>> df.columns
		      
Index(['A', 'B', 'C', 'D'], dtype='object')
>>> df.values
		      
array([[ 2.26043929,  1.5976354 , -0.12468347,  0.12856627],
       [-0.25393275,  0.87227555,  0.96787232, -1.44142558],
       [-0.75396222,  1.02833594, -0.11541912, -1.41362724],
       [-0.52772278,  0.4017487 ,  0.50524575, -1.70665845],
       [ 0.6751163 , -0.42355161,  0.6622185 , -0.22092232],
       [ 1.77430832,  0.568452  , -0.77507625,  1.30259452]])
>>> df.T
		      
   2018-01-03  2018-01-04     ...      2018-01-07  2018-01-08
A    2.260439   -0.253933     ...        0.675116    1.774308
B    1.597635    0.872276     ...       -0.423552    0.568452
C   -0.124683    0.967872     ...        0.662218   -0.775076
D    0.128566   -1.441426     ...       -0.220922    1.302595

[4 rows x 6 columns]
>>> df.describe()
		      
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.529041  0.674149  0.186693 -0.558579
std    1.260608  0.679389  0.640479  1.172925
min   -0.753962 -0.423552 -0.775076 -1.706658
25%   -0.459275  0.443425 -0.122367 -1.434476
50%    0.210592  0.720364  0.194913 -0.817275
75%    1.499510  0.989321  0.622975  0.041194
max    2.260439  1.597635  0.967872  1.302595
>>> df.T
		      
   2018-01-03  2018-01-04     ...      2018-01-07  2018-01-08
A    2.260439   -0.253933     ...        0.675116    1.774308
B    1.597635    0.872276     ...       -0.423552    0.568452
C   -0.124683    0.967872     ...        0.662218   -0.775076
D    0.128566   -1.441426     ...       -0.220922    1.302595

[4 rows x 6 columns]

>>> df.sort_index(axis=1,ascending=False)
		      
                   D         C         B         A
2018-01-03  0.128566 -0.124683  1.597635  2.260439
2018-01-04 -1.441426  0.967872  0.872276 -0.253933
2018-01-05 -1.413627 -0.115419  1.028336 -0.753962
2018-01-06 -1.706658  0.505246  0.401749 -0.527723
2018-01-07 -0.220922  0.662218 -0.423552  0.675116
2018-01-08  1.302595 -0.775076  0.568452  1.774308
>>> df
		      
                   A         B         C         D
2018-01-03  2.260439  1.597635 -0.124683  0.128566
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
2018-01-05 -0.753962  1.028336 -0.115419 -1.413627
2018-01-06 -0.527723  0.401749  0.505246 -1.706658
2018-01-07  0.675116 -0.423552  0.662218 -0.220922
2018-01-08  1.774308  0.568452 -0.775076  1.302595
>>> df.sort_index(axis=1,ascending=true)
		      
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    df.sort_index(axis=1,ascending=true)
NameError: name 'true' is not defined
>>> df.sort_index(axis=1,ascending=true)
		      
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    df.sort_index(axis=1,ascending=true)
NameError: name 'true' is not defined
>>> df.sort_index(axis=1,ascending=True)
		      
                   A         B         C         D
2018-01-03  2.260439  1.597635 -0.124683  0.128566
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
2018-01-05 -0.753962  1.028336 -0.115419 -1.413627
2018-01-06 -0.527723  0.401749  0.505246 -1.706658
2018-01-07  0.675116 -0.423552  0.662218 -0.220922
2018-01-08  1.774308  0.568452 -0.775076  1.302595
>>> df.sort_values()
		      
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    df.sort_values()
TypeError: sort_values() missing 1 required positional argument: 'by'
>>> df.sort_values(by='B')
		      
                   A         B         C         D
2018-01-07  0.675116 -0.423552  0.662218 -0.220922
2018-01-06 -0.527723  0.401749  0.505246 -1.706658
2018-01-08  1.774308  0.568452 -0.775076  1.302595
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
2018-01-05 -0.753962  1.028336 -0.115419 -1.413627
2018-01-03  2.260439  1.597635 -0.124683  0.128566
>>> df['A']
		      
2018-01-03    2.260439
2018-01-04   -0.253933
2018-01-05   -0.753962
2018-01-06   -0.527723
2018-01-07    0.675116
2018-01-08    1.774308
Freq: D, Name: A, dtype: float64
>>> df
		      
                   A         B         C         D
2018-01-03  2.260439  1.597635 -0.124683  0.128566
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
2018-01-05 -0.753962  1.028336 -0.115419 -1.413627
2018-01-06 -0.527723  0.401749  0.505246 -1.706658
2018-01-07  0.675116 -0.423552  0.662218 -0.220922
2018-01-08  1.774308  0.568452 -0.775076  1.302595
>>> df[0:3]
		      
                   A         B         C         D
2018-01-03  2.260439  1.597635 -0.124683  0.128566
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
2018-01-05 -0.753962  1.028336 -0.115419 -1.413627
>>> df['20130102':'20130104']
		      
Empty DataFrame
Columns: [A, B, C, D]
Index: []
>>> df['20180102':'20180104']
		      
                   A         B         C         D
2018-01-03  2.260439  1.597635 -0.124683  0.128566
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
>>> df
		      
                   A         B         C         D
2018-01-03  2.260439  1.597635 -0.124683  0.128566
2018-01-04 -0.253933  0.872276  0.967872 -1.441426
2018-01-05 -0.753962  1.028336 -0.115419 -1.413627
2018-01-06 -0.527723  0.401749  0.505246 -1.706658
2018-01-07  0.675116 -0.423552  0.662218 -0.220922
2018-01-08  1.774308  0.568452 -0.775076  1.302595
>>> df.loc[dates[0]]
		      
A    2.260439
B    1.597635
C   -0.124683
D    0.128566
Name: 2018-01-03 00:00:00, dtype: float64
>>> 
df.loc[:,['A','B']]
		      
                   A         B
2018-01-03  2.260439  1.597635
2018-01-04 -0.253933  0.872276
2018-01-05 -0.753962  1.028336
2018-01-06 -0.527723  0.401749
2018-01-07  0.675116 -0.423552
2018-01-08  1.774308  0.568452
>>> df.loc['20180102':'20180104',['A','B']]
		      
                   A         B
2018-01-03  2.260439  1.597635
2018-01-04 -0.253933  0.872276
>>> 
