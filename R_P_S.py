from tkinter import *
from random import randrange as rand
import tkinter.messagebox
from tkinter import ttk

#----------------------------
#simple implementation of Rock Paper Scissors game in python with a simple
#beginners' GUI
#-----------------------------------

how_to_play = '\
1. The computer makes a choice and you do the same by clicking on any of the choices\n\
2. Each win earns 3 points and each draw earns 1 point while a lose earns no points\n\
3. There are 5 rounds in each game after which the winner of the game is announced'

#0=rock, 1 = paper, 2= scissors
ROCK =      0
PAPER =     1
SCISSORS =  2

PLAYER_POINTS = 0
COMPUTER_POINTS = 0



# counting number of times played will be implemented later
def main():#init creates window and widgets
    window = Tk()
    #creating the widgets
    #------------------------------------BUTTONS--------------------
    rock_button = Button(window, text = '  ROCK  ', font = ('Times', 15), \
            command = lambda player_choice =ROCK:update_result(player_choice) ).grid(row = 0, column=0, columnspan = 10)#
    paper_button = Button(window, text = ' PAPER ', font = ('Times', 15) \
            ,command = lambda player_choice=PAPER:update_result(player_choice) ).grid(row = 0, column=12, columnspan = 10)
    sci_button = Button(window, text = 'SCISSORS', font = ('Times', 15),\
             command = lambda player_choice=SCISSORS:update_result(player_choice) ).grid(row = 0, column=24, columnspan = 10)
    help_button = Button(window, text = 'Need Help?', font = ('Times',15, 'italic'),\
                         command= showhelp).grid(row = 2, column=12, columnspan = 10)
    
    #------------------------Labels for the scores---------------
    ttk.Label(window, text = 'Computer', background = 'red').grid(row = 4, column =0, columnspan = 10)
    ttk.Label(window, text = ' Player ', background = 'blue').grid(row = 4, column = 13, columnspan = 10)



        #Lamda trick will be used
    def update_result(player_choice):#depending on which button was clicked
        global PLAYER_POINTS, COMPUTER_POINTS 
        def check_winner():
            computer_choice = get_computer_choice()
            
            if computer_choice == player_choice:
                return 0 #draw
            
            elif (computer_choice == ROCK and player_choice ==PAPER)or (computer_choice ==SCISSORS and player_choice == ROCK)\
                 or (computer_choice ==PAPER and  player_choice ==SCISSORS):
                return False #that is a loss for the computer
            elif (player_choice == ROCK and computer_choice ==PAPER)or (player_choice ==SCISSORS and computer_choice == ROCK)\
                 or (player_choice ==PAPER and  computer_choice ==SCISSORS):
                return True #that is a loss for the computer
            #else: return True #any other case is a win for the computer
        the_winner = check_winner()
        if the_winner== 0:
            PLAYER_POINTS += 1
            COMPUTER_POINTS += 1
        elif the_winner ==False:#computer lost
            PLAYER_POINTS += 3

        elif the_winner == True:
            COMPUTER_POINTS += 3
        #nonlocal COMPUTER_SCORE_LABEL,PLAYER_SCORE_LABEL
        #COMPUTER_SCORE_LABEL.configure( text = f'{COMPUTER_POINTS}')
        #PLAYER_SCORE_LABEL.configure( text = f'{PLAYER_POINTS}' )
        COMPUTER_SCORE_LABEL = Label(window, text = f'{COMPUTER_POINTS}',font = ('Times', 15)).grid(row = 5, column=0, columnspan = 10)
        PLAYER_SCORE_LABEL = Label(window, text = f'{PLAYER_POINTS}',font = ('Times', 15)).grid(row = 5, column=13, columnspan = 10)

    window.resizable(False, False)
    mainloop()#as part of the main running program

    


def showhelp():
    tkinter.messagebox.showinfo(title = 'HELP', message = how_to_play)
    
def get_computer_choice():
    return rand(0, 3) #0<=choice<3

def s(a):print(f'{a} is a number')
    
        
if __name__ == '__main__':
    main()

