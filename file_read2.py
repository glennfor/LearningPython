#try out file  I/O
myfile=open("example.txt", "a+")
secondfile=open("python.txt", "r")
for _ in range(4):
    print(secondfile.read())
