'''
encyption.py
UsAge: User enters a piece fo text, it is encypted and displayed .
uesr can also specify to decrypt the text

--the encryption code is determined by building a string of random numbers which are stored in the decryption code

--primarily only alphabetis text will be encrypted but numeric and punctuation may be added later

--encrption is carried out by shifting individual alphabetic charaters the corresponding number of times specified in the
  encryption code
--NOTE: the lenght of the code string must be the sanme as the message string to be encyrpted

--May be quite challenging but what's there?

--this encryption is quite limited but can be improved later
--mainly the cases not handled
1.->CASES(upper and lowercase)
2.->WHITE_SPACES(newlines, spaces, tabs, ...
3.->PUNCTUATION(all punctuation characters from string.punctuation
4.->NUMBERS(0 ,1 ,2, 3, 4, 5, 6,7,8,9) 

--Also, all message scan only be dealt with as uppercase but in the future the encryption algorithm will be able to
  restore the message as it was primarily-->using all the ascii_letters in the check list
    ------------------------->HALLELUJAH<------------------------------------------
  ----->THANK THE GOD FOR NEGATIVE INDICES ELSE HOW MUCH WORK I WOULD HAVE HAD<---------------
  ---------------------------->HALLELUIA<-------------------------------------------


  '''

from string import ascii_letters, punctuation
from random import randint as rand, randrange

#checklist and numbercode list are rightfully declare as global variables
check=ascii_letters[-26:]#ideally capital letters
check=list(check)#actually equivilent-->check=list(ascii_letters[-26:])
numbers=[i for i in range(1,27)]#backup code

def encrypt(message, code):
    send=''
    for char in message:
        send += shifted(char.upper(), code[message.index(char)])#dealing only with capital letters
    return send
#return ''.join(shifted(char.upper(), code[message.index(char)]) for char in message)

def shifted(character, number_of_times_to_shift):#note that both parameters are strings
    shift_this_number_of_times=int(number_of_times_to_shift)
    initial_position_of_char=check.index(character)
    return check[(initial_position_of_char + shift_this_number_of_times)%26]

#here is the real deal --->no doubt this is the hardest part of the exercise but what's there? HWPO-->PO-->FUIG
#decrypt receives as argument the encrypted text and the code used to encrypt tthe text
def decrypt(sent, code):
    the_initial_message=''#this should yield the original text that was encrypted
    for everychar in sent:
        #note that the char is not 'uppercased' because it was already during the encrption process
        the_initial_message += deshifted(everychar.upper(), code[sent.index(everychar)])
    return the_initial_message

#actually the deshifted function WOULD HAVE been the toughest part of this decryption process
#BUT THANKS TO GOD FOR NEGATIVE INDICES
		

def deshifted(character, number_of_times_to_shift):#note that both parameters are strings
    unshift_this_number_of_times=int(number_of_times_to_shift)
    initial_position_of_char=check.index(character)
    return check[(initial_position_of_char - unshift_this_number_of_times)%26]


#-----------------------------------------------------------------------------------------------------------------
#NOW, i will write a real program to do the implement the encryption proper----------------------------------
#Simulates encryption and decryption in real life
#----------------------------------------------------------------------------
message=input('Enter text to encrypt:  ')
code_builder=([rand(1,9) for _ in range(len(message))])
code=''
for eachnumber in code_builder:
    code += str(eachnumber)#concatenate the stringized form of each numbernuber in the code_builder
print("Conversion code(Decryption key): -->"+code)
print('The message: '+message)

output=encrypt(message, code)# at the sending end
#SEND
print('Encryted form: '+output)

decrypted_original=decrypt(output, code)#at the receiving end
print('After decryption:  '+decrypted_original)
print(punctuation)




