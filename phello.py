print ("HELLO WORLD")

def sleep_in(weekday, vacation):
    if not weekday or vacation :
        return True
    return False

def string_times(st, num):
    return st*num


print(string_times('HELLO, ', 4))

def first_last6(alist):
    if 6 in (alist[0], alist[-1]):
        return True
    return False

list1=[1,2,6]
list2=[6, 5,6]
list3=[2,3,4]
list4=[2,6]
print(first_last6(list1))
print(first_last6(list2))
print(first_last6(list3))
print(first_last6(list4))

def double_char(mystr):
    ret=''
    for char in mystr:
        ret += char*2
    return ret

print(double_char('Hey-There'))


def count_evens(mylist):
    count=0
    for num in mylist:
        if not num%2: count +=1

    return count

import random
print(count_evens(list(random.randint(1,20) for _ in range(1,20))))

def weirdo(st):
    retval=''
    for i in range(len(st)):
        retval +=st[:i+1]+' '

    return retval

print(weirdo('Elvis'))
