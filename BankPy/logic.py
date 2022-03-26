import random





'''
use luhns algorithm to validate a 16-digit card number
return: boolean:validated, string:error
'''

def validateCardNumber(cardNo):
    try:
        int(str(cardNo))
    except ValueError:
        return False, "Card No Must Contain Only digits"

    cardNo = str(cardNo)
    if len(cardNo)!=16:
        return False, "Wrong Length : Expected 16 digits"
    #use the algorithm to validate now
    checkDigit = int(cardNo[-1])
    checkSum = 0
    for pos , value in enumerate(cardNo[:-1], start=1):
        value=int(value)
        value = value if(pos%2==0) else value*2
        value = value if(value<10) else value-9
        checkSum += value

    valid = (checkSum+checkDigit)%10==0
    
    return  ((True, "Card Number is Valid") if (valid)else(False, "Card Number is NOT valid"))


def generateValidCardNumber():
    allNumbers = "0123456789"
    IIN = '400000'
    cardDigits = IIN
    for _ in range(9): #first 15 digits
        cardDigits += random.choice(allNumbers)

    #get the check sum for these digits
    checkSum = 0
    for pos , value in enumerate(cardDigits, start=1):
        value = int(value)
        value = value if(pos%2==0) else value*2
        value = value if(value<10) else value-9
        checkSum += value
        
    checkDigit = 10 - (checkSum%10)

    return cardDigits+str(checkDigit)





class BankAccount(object):
    def __init__(self, cardNo, pin):
        self.deposit = 0.0
        self.cardNo = cardNo
        self.PIN = pin

    def withDraw(self, amount):
        self.deposit -= amount

    def deposit(self, amount):
        self.deposit += amount

    def balance(self):
        return self.deposit



