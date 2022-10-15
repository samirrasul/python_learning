from csv import list_dialects


lst = ['Samir', 'Jacob', '9', '3', '0', '14'];
'''
for x in lst:
    print(x);
'''
'''
for i in range(len(lst)):
    print(lst[i]);
'''
'''
lst_updated = lst.pop(2)
print(lst)
'''
'''
i = 0;
while i < len(lst):
    print(lst[i]);
    i = i + 1;
'''
list = [];
'''
for x in lst:
    if "o" in x:
        list.append(x);
print(list)

list = [x for x in lst if type(x) != int];
print(list)
'''
list = [x for x in range(3)]
print(list)