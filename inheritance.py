class Person:
    def __init__(self, name, surname):
        self.first_name = name
        self.second_name = surname
    def print_name(self):
        print(self.first_name, self.second_name)
x = Person("Joe", "Hossain")
x.print_name()

'''class Student(Person):
    def __init__(self, name, surname):
        Person.__init__(self, name, surname)'''

class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.graduationyear = 2022

    def welcome(self):
        print("Welcome", self.first_name, self.second_name, "to the class of", self.graduationyear)
x = Student("Joe", "Hassan")
x.welcome();
