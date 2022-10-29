str = '34 23 45 45 345 234 56 56 567 5 123 1 3'
str1 = ''
list1 = list([])
for x in str:
    if x != ' ':
        str1 = str1 + x
    else:
        list1.append(int(str1))
        str1 = ' '
print(list1)
