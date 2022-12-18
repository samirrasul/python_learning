class user_manager:
    user_dict = dict()
    next_id = 0
    def sign_up(self, **kwargs):
        name = kwargs["name"]
        surname = kwargs["surname"]
        if self.user_dict.keys():
            self.next_id = max(self.user_dict.keys()) + 1
            self.user_dict[self.next_id] = {
                "name" : name,
                "surname" : surname
            }
        else:
            self.user_dict[0] = {
                "name" : name,
                "surname" : surname
            }
        return self.user_dict[self.next_id]
Person = user_manager()
print(Person.sign_up(name = "Jacob", surname = "Hossain"))
print(Person.sign_up(name = "Elzabeth", surname = "Rossad"))
print(Person.sign_up(name = "Patrick", surname = "SpongeBob"))
print(Person.user_dict)