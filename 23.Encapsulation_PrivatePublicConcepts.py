class myClass:
    __myPrivateVariable = 0  # two underscore indicates that it's a private member variable
    myPublicVariable = 0     # this is my normal member variable

    def __init__(self):                # Constructor of a class will be called when the object of a class is created
        self.__myPrivateVariable = 10  # Changing the private member value in Constructor
        self.myPublicVariable = 100

    def showVariable(self):
        print 'Private Variable Value =', self.__myPrivateVariable
        print 'Public Variable Value =', self.myPublicVariable

    def setPrivateVariable(self, value):
        self.__myPrivateVariable = value


classObject = myClass()              # Creating an object of a class
# Now, Trying to access and change the private member variable which is not possible
classObject.__myPrivateVariable = 20
classObject.myPublicVariable = 200  # Trying to access and change the public member which is possible
classObject.showVariable()          # I will be able to change the public member variable only

# I can change the private variable value by using class member function
classObject.setPrivateVariable(30)  # Setting private member value to 30
classObject.showVariable()
print 'Accessing private variable directly:', classObject._myClass__myPrivateVariable
# Private members can not be accessed outside the class but can be accessed using methods of the class
# or using object._className__attrName
