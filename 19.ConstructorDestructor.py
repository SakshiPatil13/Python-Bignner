class Person:
    def __init__(self):
        print("Object is created. So constructor is called automatically.")

    def __del__(self):
        print("Object is destroyed.")

    def setName(self, firstName, lastName):
        self.firstName = firstName  # need to create self object within the class
        self.lastName = lastName    # and it will be used all over the class like global variable

    def showName(self):  # self argument is always present in any member function arguments
        print 'In class, showName method:', self.firstName, self.lastName


name = Person()  # creating object of Person class. freaky method...he he. its not like java
# to pass the arguments to the constructor we have to write name = Person(arguments)
# how strange but the destructor can also take the arguments!!!
name.setName("Prasad", "Dalavi")
name.showName()
