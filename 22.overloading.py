class Human:
    def sayHello(self, name=None):

        if name is not None:
            print 'Hello ' + name
        else:
            print 'Hello '


obj = Human()           # Create instance
obj.sayHello()          # Call the method
obj.sayHello('Guido')   # Method overloading i.e. same method is called but with different parameter
