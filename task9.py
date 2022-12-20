def get_Fibonacci_series_till_given_number(max):

    count = 0
    number1 = 0
    number2 = 1

    if max == 0:
        print(0)
    
    if max == 1:
        print(1)

    else:
        while(count < max):
            print(number1)
            next_number = number1 + number2
            number1 = number2
            number2 = next_number
            count = count + 1

print(get_Fibonacci_series_till_given_number(10))

