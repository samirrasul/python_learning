import random


def guess_the_number():

    number = random.randint(1, 100)
    input_number = int(input("Enter the initial guessing: "))
    print(number)
    
    while(True):
        
        if number == input_number:
            print("Congratulations!!!")
            quit()

        if input_number > number:
            input_number = int(input("Go down: "))
        
        if input_number < number:
            input_number = int(input("Go up: "))


guess_the_number()
