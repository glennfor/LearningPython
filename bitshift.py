#/*Exercise 11-6: Write a program that will take all the bits in a number and shift them to the left
#end. For example, 01010110 (binary) would become 11110000 (binary).*/

from math import log2, floor

print()
print("This program that left-shifts all the 'ON' bits in a binary number")
number=int(input('Enter a binary number:  '), 2)#takes input in base 2
#was already astring . converted to number and back to string just for fun
result = ''.join(sorted(str(number)[2:])[::-1])
print(result)
print('After shifting{:%d}, the result is{:%s}'%(number, '0b'+result))
