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
        
        self.string = string


    def get_string(self):

        return self.string
    
    def validate(self, value):
        
        if type(value) == str:
            print(True)
            self.string = value

        else:
            print(False)
            quit()
    
string1 = String()
string1.validate(True)
#string1.set_string(6)
print(string1.get_string())

