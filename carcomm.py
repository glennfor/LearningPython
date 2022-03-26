state=False#false here means the car is already stopped
while True:
    command=input('> ')
    command=command.lower()
    #or just:: command=input('> ').lower() directly
    if command.upper()=='HELP':
        print('Start - To start engine')
        print('Stop - To stop engine')
        print('Quit - To exit')
    elif command=='start':
        if state==False:#if not state(ie if state is false
            print("Car engine started , We are good to go...")
            state=True#engine is on
        else:
            print("Invalid-->Car engine was already started")
    elif command=='stop':
        if state==True:
            print('Car engine stopped...')
            state=False
        else:
            print("Invalid-->Car engine was already stopped...")
    elif command=='quit':
        break #break out of loop and terminate prgram
    else:
        print("I don't understand that ...")

