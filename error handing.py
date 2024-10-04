try:
    number = int(input('enter a number : '))
    print (f'you entered number is {number}')
except ValueError:
    print('you entered invalid number')