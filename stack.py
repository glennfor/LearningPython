#Stack implementation in python

class Stack(object):
    "Class to implement a stack using a list"
    "end of list is considered top of the stack"
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items[:]==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __getall__(self):
        return self.items



newStack = Stack()
newStack.push(12)
newStack.push(True)
newStack.push((12,34))
newStack.push({1,2,3,4})
newStack.push([i for i in 'JESUS'])
newStack.push({chr(k):v for k in range(ord('A'), ord('Z')+1) for v in range(1,26+1)})

while True:
    choice =input('1. Enter element in to Stack\n'+
    '2. Return element from Stack\n'+
    '3. Get size of Stack\n'+
    'any other character stops process\n')[0]
    if choice=='1':
        entry = input('Enter the element:  ')
        try:
            entry = eval(entry)#gets any datatype, 
        except (ValueError,NameError):
            pass
        else:
            newStack.push(entry)
    elif choice == '2':
        print(newStack.pop(), ' returned')
    elif choice == '3':
        print('Stack has ',newStack.size(),'elements')
        print('Elements are ',newStack.__getall__())
    else:
        break

