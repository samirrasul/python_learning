this_dict = {
    "name" : "Jacob",
    "age"   : 15,
    "gender"    : "male"
}
'''print(this_dict["age"]);
print(len(this_dict))'''
all_keys = this_dict.keys();
print(all_keys)
this_dict["surname"] = "Hossain";
print(all_keys)
print(this_dict.items())
print(this_dict.popitem())
print(this_dict)