class Parent1:
    value1 = "this is value 1"
    value2 = "this is value 2"


class Parent2:
    value3 = "this is value 3"
    value4 = "this is value 4"


class Child (Parent1, Parent2):  # extending derived class from base classes
    pass


parent1_object = Parent1()     # creating an object of parent class
print(parent1_object.value1)
print parent1_object.value2

child_object = Child()  # creating an object of child class
print("Now Printing the value using child or base class")
print(child_object.value3)
print(child_object.value4)
