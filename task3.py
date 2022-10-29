path_name = "C:\\Users\\samir\\Desktop\\"
f = open(path_name + "umber.txt", "r")
str1 = ''
list = []
#print(f.readlines())
for x in f.readlines():
    list1 = x.split(' ')
    #print(list1)
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i] == list1[j] and i != j:
                list.append(list1[j])
            else:
                continue
print(list)