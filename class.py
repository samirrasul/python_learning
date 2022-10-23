'''class My_class:
    x = 5
p1 = My_class() 
print(p1.x)'''

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Hossain ", 34)
print(p1)'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    def my_func(self):
        print('My name is: ', self.name)
p1 = Person("Jacob", 93)
p1.my_func()
p1.age = 39
print(p1)
