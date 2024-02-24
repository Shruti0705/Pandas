import pandas as pd


list_s = [1,2,-3,6.2, 'data values']
print(list_s)

series1 = pd.Series(list_s)
print(series1)


#series in short

series2 = pd.Series([1,2,3,-4])
print(series2)


#empty list

empty_s = pd.Series([])
print(empty_s)


#change the default index of the series given by series data structure

series3 = pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd'], dtype = float)
print(series3)


#we can give a name to the column of data values

series4 = pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd'], dtype = float, name = 'data values')
print(series4)


#we can create series using scalar value means single value

scalar_s = pd.Series(0.5)
print(scalar_s)

#to give the index for this scalar value

scalar_s = pd.Series(0.5, index = [1,2,3])
print(scalar_s)


# we can also create series using dictionery

dict_s = pd.Series({'a':1, 'b':2})
print(dict_s)


#operators

s4 = pd.Series([1,2,3,4,5])
print(s4)
print(s4[0])


#slice

print(s4[0:3])

#maximum value in s4

print(max(s4))


#minimum value in s4

print(min(s4))


#condition

print(s4[s4 > 3])

#mathematics operations

s5 = pd.Series([1,2,3,4,5])
print(s5)

print(s4+s5)


#for operations with unequa; data values

s6 = pd.Series([1,2,3])
print(s6)


print(s5+s6)




