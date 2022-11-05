def shout(text):
    return text.upper()
def greeting(func):
    greeting = func("Hi, this is for testing")
    print(greeting)

greeting(shout)

