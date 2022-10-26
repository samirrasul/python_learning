'''mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))'''

'''class Mytuple:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = Mytuple();
my_iter = iter(myclass)
print(next(my_iter))
print(next(my_iter))'''

class My_tuple:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_class = My_tuple()
my_iter = iter(my_class)

for x in my_iter:
    print(x)