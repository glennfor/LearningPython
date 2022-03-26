#Queue implementation python

class Queue:
    "Class implementing a  queue using python list"
    "the end of stack is for dequeueing"
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items == []  #or len(self.items)==0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop() if not self.is_empty() else 'Queue Underflow'

    def size(self):
        return len(self.items)

    def __getall__(self):
        return self.items


#trying out the queue proper

newQueue = Queue()
newQueue.enqueue(12)
newQueue.enqueue(True)
newQueue.enqueue((12,34))
newQueue.enqueue({1,2,3,4})
newQueue.enqueue([i for i in 'JESUS'])
newQueue.enqueue({chr(k):v for k in range(ord('A'), ord('Z')+1) for v in range(1,26+1)})
while True:
    choice =input('1. Enter element in to queue\n'+
    '2. Return element from queue\n'+
    '3. Get size of queue\n'+
    'any other character stops process\n')
    if choice=='1':
        entry = input('Enter the element:  ')
        try:
            entry = eval(entry)#gets any datatype, 
        except (ValueError, NameError):
            pass
        newQueue.enqueue(entry)
    elif choice == '2':
        print(newQueue.dequeue(), ' returned')
    elif choice == '3':
        print('Queue has ',newQueue.size(),'elements')
        print('Elements are ',newQueue.__getall__())
    else:
        break

