def GCD(number1, number2):

    result = 1

    if number1 % number2 == 0:
        return number2
    elif number2 % number1 == 0:
        return number1
    for i in range(int(number2/2), 0, -1):
        if number1 % i == 0 and number2 % i == 0:
            result = i
            break
    return result

print(GCD(56, 128))