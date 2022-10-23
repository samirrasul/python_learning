'''number = lambda n, y: n*(n+y);
print(number(12, 12))
n = lambda x: x*x;
print(n(34))'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(12))
