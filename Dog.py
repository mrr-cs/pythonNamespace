# blueprint
class Dog:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
 
    def bark(self):
        return "The " + self.breed + " called " + self.name + " is barking."

# The "self" variable gives us access to the current instance and properties.
dog1 = Dog("labrador", "Bob")
print(dog1.bark())

dog2 = Dog("labradoodle", "Wally")
print(dog2.bark())

