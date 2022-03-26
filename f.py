#print an F
numbers=[5,2,5,2,2]
for x in range(len(numbers)):
    for y in range(numbers[x]):
        print('*',end='')
    print()
#Alternatively
    '''
numbers=[5,2,5,2,2]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output+='*'
    print(output)

    '''

print()
print()
print()
#print an 'L'
lnum=[2,2,2,2,5]
for x_count in lnum:
    output=''
    for count in range(x_count):
        output+='*'
    print(output)
