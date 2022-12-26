def histogram(list):
    
    for value in list:
        output = ' '
        count = 0
        while(count != value):
            output = output + '@'
            count += 1
        print(output)

histogram([1, 2, 3, 4, 5, 4, 3, 2, 1])