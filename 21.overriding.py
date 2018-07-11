class Parent:
    def my_method_1(self):
        print 'This is parent class method 1'

    def my_method_2(self):
        print 'This is parent class method 2'


class Child(Parent):        # Child class inheriting the properties from parent class
    def my_method_2(self):
        print 'This is child class method 2'


child_object = Child()
child_object.my_method_1()  # Child class using Parent class properties (methods)
child_object.my_method_2()  # Parent class method has been overrided by Child class
