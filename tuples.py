'''
tuple = ("Jacob",);
print(type(tuple));

tuple1 = ('fran', 'moji', 'trab');
list1 = list(tuple1);
'print(list1)'
list1[1] = "Hello";
tuple2 = tuple(list1);
print(tuple2)

tuple1 = ("Sam", "Jacob", "Hossain");
tuple2 = ("Francia",)
tuple1 = tuple1 + tuple2;
print(tuple1);
'''
tuple1 = ("alma", "paradicsom", "sargarepa", "hagyma");
(green, *red, yellow) = tuple1;
print(red)