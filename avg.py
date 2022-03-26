##############################################################3
#PROGRAM TO CALCULATE THE AVERAGE OF ANY NUMBER OF NUMBRES######
#############################################################

print("This Program Calculates the average for any number of numbers")
print("Enter the numbers-->(Enter a non-digit character to stop input")
total=0
counter=0
while True:
    try:
        num=float(input(''))
    except ValueError:
        break
    else:
        total +=num
        counter +=1
try:
    avg=total/counter
except ZeroDivisionError:
    avg=0

print(f'The average of the above numbers is {avg}')
        
    
