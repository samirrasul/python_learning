def LCM(number1, number2):

    if number1 % number2 == 0:
        return number1

    elif number2 % number1 == 0:
        return number2
    
    result = 1

    for i in range(0, int(number1*number2 + 1), 1):
        
        if i % number1 == 0 and i % number2 == 0 and i != 0:
            result = i
            break
    return result

print(LCM(13, 144))