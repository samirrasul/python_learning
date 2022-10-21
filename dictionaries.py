"""this_dict = {
    "name" : "Jacob",
    "age"   : 15,
    "gender"    : "male"
}
'''print(this_dict["age"]);
print(len(this_dict))
all_keys = this_dict.keys();
print(all_keys)
this_dict["surname"] = "Hossain";
print(all_keys)
print(this_dict.items())
print(this_dict.popitem())
print(this_dict)'''

new_dict = this_dict.copy();
print(new_dict)"""

person_1 = {
    "name" : "Jacob",
    "surname" : "Hossain",
    "age" : 34
}
person_2 = {
    "name" : "Jacob",
    "surname" : "Hossain",
    "age" : 34
}
person_3 = {
    "name" : "Jacob",
    "surname" : "Hossain",
    "age" : 34
}
people = {
    "person_1" : person_1,
    "person_2" : person_2,
    "person_3" : person_3
}
print(people);
