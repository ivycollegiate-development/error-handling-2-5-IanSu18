try:
    num1 = int(input('Please enter a number'))
except ValueError:
    print('I am sorry, but that is not a valid number,')



print(f'The number that you input:{num1}')