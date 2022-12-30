class String:
    """
    A class to represent string.

    ...

    Attributes
    ----------
    string : str
        arbitrary string to input

    Methods
    -------
    set_string(string):
        Generates a string.
    get_string():
        Prints the string generated.
    """

    def set_string(self, string):
        
        if self.validate(string):
            self.string = string
        else:
            raise TypeError("Only strings are allowed")


    def get_string(self):

        return self.string
    
    def validate(self, value):
        
        if not type(value) == str:
            return False
        return True
    
string1 = String()
string1.set_string("12")
#string1.set_string(6)
print(string1.get_string())

