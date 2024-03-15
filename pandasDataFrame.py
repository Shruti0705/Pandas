#how to create python pandas dataframe

import pandas as pd

emt_df = pd.DataFrame()
print(emt_df)


lst = ['a', 'b', 'c']
print(lst)

#create dataframe by using this list

df = pd.DataFrame(lst)
print(df)

ls_of_ls = [[1,2,3], [2,3,4], [4,5,6]]
print(ls_of_ls)


df2 = pd.DataFrame(ls_of_ls)
print(df2)

dict1 = {'ID':[11,22,33,44]}
print(dict1)

df3 = pd.DataFrame(dict1)
print(df3)

dict1 = {'ID':[11,22,33,44], 'SN':[1,2,3,4]}
print(dict1)



#list of dictionery

lists_dict = [{'a':1, 'b':2}, {'a':3, 'b':4}]
df5 = pd.DataFrame(ls_dict)
print(df5)


ls_dict = [{'a':1, 'b':2}, {'a':3, 'b':4, 'c':5}]
df5 = pd.DataFrame(ls_dict)
print(df5)



dict_sr = {'ID': pd.Series([1,2,3]), 'SN': [111,222,333]}
df6 = pd.DataFrame(dict_sr)
print(df6)







































