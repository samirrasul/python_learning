lst = [True, 'Jacob', 0];
print(type(lst));

lst = list((True, False, 0, 92, 'Jacob', None));
print(lst);

print(lst[-4:-1])
lst[2] = "True"
lst[3:4] = "True", "Maga"
lst.insert(5, "Optics")
lst.append("Hanka")
print(lst)