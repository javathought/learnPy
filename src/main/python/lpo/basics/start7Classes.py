class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then pring out both values
print(myobjectx.variable)
print(myobjecty.variable)
myobjectx.function()

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.0
car1.name = 'Fer'

car2 = Vehicle()
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.0
car2.name = 'Jump'

# test code
print(car1.description())
print(car2.description())
