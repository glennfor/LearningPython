#python program to print a multpliction table
print("PROGRAM TO PRINT A MULTIPLIACTION TABLE\n")

column=input("Enter number of coloumns:   ")
rows=input("Enter number of rows:     ")
col=int(column)
row=int(rows)
col+=1
print(end='      ')#that is 4 spaces
for y in range(1,col):
    print ("{: >4d}".format(y),end='  ')
print()
for _ in range (0, 6*col):
    print('-',end='')
print()
for x in range(1,row+1):
    print("{: >4d}".format(x) ,end="  ")
    for y in range(1,col):
        print("{: >4d}".format((x*y))  ,end='  ')
    print()
