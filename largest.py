#program to print largest number in alist

numbers=[12,33,45,11,1,3,0,455,89,678]
max=numbers[0]
for index in range(len(numbers)):
    if numbers[index]>=max:
        max=numbers[index]
print(f'The maximum number in the list {numbers} is {max}')

#Alternative solution
'''
for number in numbers:
    if number>=max:
        max=number
print(f'The maximum number in the list {numbers} is {max}')
'''
