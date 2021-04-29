def omari_calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Enter your first number: '))
    #when you put int it tells the pc "yo nigga numbers only"
    #and tells the print function to calculate what you give it
    number_2 = int(input('Enter your second number: '))
    #formating it makes it look snazzy
    
    #MAKE SURE TO ADD INDENTATION, NOTHING WORKS WITHOUT THEM
    
    #addition
    if operation == '+':
        print(' {} + {} = '. format (number_1, number_2))
        print(number_1 + number_2)
    
    
    #subtraction
    elif operation == '-':
        print(' {} - {} = '. format (number_1, number_2))
        print(number_1 - number_2)
    
    #multiplacation
    elif operation == '*':
        print(' {} * {} = '. format (number_1, number_2))
        print(number_1 * number_2)
    
    #division
    elif operation == '/':
        print(' {} / {} = '. format (number_1, number_2))
        print(number_1 / number_2)
    
    else:
        print('No Nigga.')

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        omari_calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

omari_calculate()