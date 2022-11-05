'''import time
import math

def calculate_time(func):

    def inner1(*args, **kwargs):
        begin = time.time()

        func(*args, **kwargs)

        end = time.time()
        print("Total time", func.__name__, end - begin)

    return inner1

@calculate_time

def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(28)'''

def decor2(func):
    def inner():
        x = func()
        return x*x
    return inner
    
def decor1(func):
    def inner():
        x = func()
        return 2*x
    return inner
@decor2
@decor1

def num():
    return 10
print(num())


