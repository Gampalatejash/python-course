# read mode
file=open('hello.txt',"r")
print(file.read())
# write mode
file=open('hello.txt',"w")
file.write('electornics and communication egineering')
file.close()
file=open('hello.txt','r')
print(file.read())
# append mode
file=open('hello.txt',"a")
file.write(' final year')
file.close()
file=open('hello.txt','r')
print(file.read())