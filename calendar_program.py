
import calendar   #import calendar module

print("This Program Creates and Displays a Calendar of months for any year after 1970 and before 2039")
  #later after 1900
while True:
    try:
        year = int(input("Enter the Calendar Year: "))
    except ValueError:
        print("Invalid Entry")
    else:
        if 1970 <= year < 2039 : break
        else:
            print('Year Range:(1970-2038)')

print()  #blank line
while True:
    try:
        month = int(input("Enter the first month to start from:  "))
    except ValueError:
        print("Invalid Entry")
    else:
        if 0 < month < 13: break
        else:print('Dummy, Month Range is 1...12')
print()  #blank line
for _ in range(3):  #  user is given a total of three chances
    try:
        number = int(input('Enter number of months to print the calendar: (MAXIMUM is 12): > '))
    except ValueError:
        print('Invalid Entry')
    else:
        if number > 12:
            print('Maximum is 12: DEFAULT=2')
            number = 2
            break
        else: break #if all input is good
else:
    print('You are not serious!!! DEFAULT=2')
    number=2

for cal in range(number):
    print()
    if month+cal <= 12:
        display = calendar.month(year, month+cal)
          #pass
    else:  #correct from here later
        month = cal
        year += 1
        display = calendar.month(year, cal-month+number)
    print(display)

