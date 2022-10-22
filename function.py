'''
def my_first_function():
    print("This is the first function");

my_first_function();

def func(language):
    print(language + " language");

func("Hungarian")

def func(*kid):
    print("This is the second child: ", kid[2]);
func("Tobias", "Jacob", "Hossain");

def func(child1, child2, child3):
    print(child3);
func(child1 = "Tobias", child2 = "Jacob", child3 = "Hossain");

def func(**kid):
    print("This is the surname:", kid["second_name"]);
func(first_name = "Dorian", second_name = "Gray")'''
'''def func(country = "Norway"):
    print("I am from", country);
func("Azerbaijan")

def func_2(number):
    return 5 * number;
print(func_2(196))'''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6);