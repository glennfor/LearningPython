import operator

'''
    LEarning how to deal with python datatypes especially with non-primitive types
'''
#Datatypes are: int, float, string,
#collection datatypes:  dictionaries , tuples , lists, sets , frozensets, 

dictionary={'Name':'Johnn Glenn', 'Age':16, 'Height':1.6, "Level":'LSS'}
tup=('Computer', 'Physics', 'Mathematics', 'Further Mathematics', 'Chemistry')
mylist=['Software Engineering', 200000, 'Google-Microsoft-NASA-Amazon']
myset=set(tup)
otherset=frozenset(mylist)
print(dictionary)
print(tup)
print(myset)
print(otherset)
print(mylist)
print(dictionary['Name'])
print(tup[:4])
print()

def factors_of(n):
    return set([i for i in range(1,n+1) if not n%i])

#----A LITTLE ON SETS-----
#creating sets
factors = set()
aset = set(range(10))
print(factors_of(500))
print(aset)
