

for num in range(1, 11):
    if num == 5:
        break  
    
    if num % 2 == 0:
        continue  
    
    print(num) 
# 2
for i in range(1):  
    for j in range(5):  
        print('*', end=' ')  
    print()  
# 3
num =[]
for num in range(1,21):
    if num%4==0:
        continue
    if num >15:
     break
    print(num)
number=[]
for number in range(1, 21):
    if number % 4 == 0:
        continue  # Skip numbers divisible by 4
    if number > 15:
        break  # Stop the loop if number is greater than 15
    print(number)

