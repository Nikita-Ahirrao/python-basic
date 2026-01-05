#Class and Object
class Employee:            # We are defining a class named Employee (class has to be in lowercase)
    name = "John"          # name and age are called attributes of the class 
    age = 26

emp = Employee()           # emp is an object of class
type(emp)            # we can cross check the data type of emp (ignore the __main__ in output, it represents the current file)

# Object of a class can access attributes of the class

print(emp.name)    
print(emp.age)

### Attributes and Methods
# Let's define one method 
# Method is also part of class, so it should have the indentation as well

class Employee:            
    name = "Sana"          
    age = 26

    def hello(self):       # self is nothing but the object that is calling this function.   
      print("Hello")

emp = Employee()           
emp.hello()                 # when this is called, the emp object is passed as self above

# The above code is correct, but we'd like to pass name and age when we create object. 
# So this is how we'll modify the code

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def details(self):
        print("Employee Name: ",  self.name)
        print("Employee Age: ", self.age)
 

emp1 = Employee("John", 26)         # creating object named emp1  --> the arguments are passed to init() automatically, and emp1 automatically gets name and age properties as passed
emp2 = Employee("Jane", 24)         # creating object named emp2  --> here also the arguments are passed to inti() without explicit calling

emp1.details()
emp2.details()

#Some examples
class Student:
    def __init__(self, name):
        self.name = name         # the right side name is coming from the argument in the init(). While with the left side name we are defining a new property for the object and assigning value to that property with right side name

    def intro(self):
        print('Hi I am', self.name)

    def change_name(self, name):
        self.name = name

john = Student('john')

# access method
john.intro()

# access attribute
print(john.name)

# change name
john.change_name('JJOOHHNN')
john.intro()

##'
class Rectangle:
    def __init__(self, length, width ):
        self.length = length
        self.width = width
    def area(self):
        print(f"Length - {self.length}, Width - {self.width}")
        return self.length * self.width

first = Rectangle(5,2)
print(first.area())

##
class Dog:
  def __init__(self, breed, age, color):
    self.breed = breed
    self.age = age
    self.color = color
  def details(self):
    print(f"Breed - {self.breed}, Age - {self.age}, Color - {self.age} ")

dog1 = Dog('Husky', 5, 'Blank')

dog1.details()

