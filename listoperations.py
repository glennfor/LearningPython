#dealing with lists

numbers=[]
print('PROGRAM TO CARRY OUT SOME OPERATIONS ON LISTS(analogous to arrays in C/C++)')
print('1. SORTING...')
num=int(input('Enter number of elements to sort: '))
print('Now, Enter the elements one by one :')
for _ in range(num):
    x=int(input(''))
    numbers.append(x)#add x to the empty list
#now to sort the elements
print('Elements in ascending order: ',end='')
for i in range(num):
    for j in range(num-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print(f'List after sorting --> {numbers}')
print()#empty line
print('2. SEARCHING ...')
target=int(input('Enter element to search in th above list: '))
if target in numbers:
    pos=numbers.index(target)
    print(f'{target} found at position {pos}')
else:
    print('Element is not present in the list !!')
print()#emty line
print('3. REMOVING an element from the list...')
target=int(input("Enter an element to remove from the list: "))
if target in numbers:
    numbers.remove(target)
    print(f'List after {target} was removed is {numbers}')
else:
    print(f"invalid operation-->{target} is not found in the list")
