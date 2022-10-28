
#file_name = "C:\\Users\\samir\\Desktop\\umber.txt"

'''f = open(file_name, "r")
for x in f:
    print(x);
f.close()'''

'''f = open(file_name, "a")
f.write("34")
f.close()

f = open(file_name, "r")
print(f.read())'''

#f = open("C:\\Users\\samir\\Desktop\\my_file.txt", "x")
import os
#os.remove("C:\\Users\\samir\\Desktop\\my_file.txt")
if os.path.exists("umber.txt"):
    os.remove("umber.txt")
else:
    print("Doesn't exist!")

