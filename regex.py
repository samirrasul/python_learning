import re

txt = "The rain in Spain"
x = re.search("The.*Spain", txt)
if x:
    print("Yes, it exists")
else:
    print("No, it doesn't exist")

y = re.findall("[arn]", txt)
print(y)