file_name = "C:\\Users\\samir\\Desktop\\umber.txt"
f = open(file_name, "r")

str1 = ''
list1 = list([ ])
for x in f:
    for y in x:
        if y != ' ':
            str1 = str1 + y
        else:
            list1.append(str1)
            str1 = ''
#print(list1)

path_name = "C:\\Users\\samir\\Desktop\\"
n = open(path_name + "new_file.txt", "w")

list2 = []
for x in list1:
    if int(x) %3 == 0 or int(x) %5 == 0 or int(x) %15 ==0:
        n.write(x + ' ')
    else:
        continue
n.close()

n = open(path_name + "new_file.txt", "r")
print(n.read())
