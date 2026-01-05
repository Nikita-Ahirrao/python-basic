#Functions
def hello():
    print("Hello World !!")
hello()    

# Let's pass some argument to the function

def hello (name):
  print(f'hello {name}')    # Note, the function body is limibted by indentetation. As long as it is there, it's a part of function body. 

hello('Ashu')
hello(22)
print(type(hello))

# Let's define a function that can carry out addition

def addthis(first, second):
  print(first + second)

addthis(12, 13)

def hello_you(name):
    return (f'hello {name.upper()}')
print(hello_you('Students'))
#Return statement
#Almost all the time, function returns some value/data
def hi(name):    
    message = "Hi "+name  
    return message  

name = input("Enter the name:")    
print(hi(name))

def add():  
    a = 40  
    b = 30  
    c = a+b  
    return c  

print("The sum is:", add())

def add(a,b):  
    return a+b; 

a = int(input("Enter a: "))    # will give error if you pass string here
b = int(input("Enter b: "))    
    
print("Sum = ",add(a,b)) 

#Let's write a function to calculate interest on loan
p = int(input("Enter the principle amount? "))    
r = float(input("Enter the rate of interest? "))     # sometimes interest rate could be in fraction like 8.5 or something, so float
t = int(input("Enter the time in years? "))

def simple_interest(p,t,r):    
    return (p*t*r)/100    

print("Simple Interest: ",simple_interest(p,r,t))

# For readability, you can call function by writing the name of arguments

def find_distance(speed, time):        
    print(speed, time)
    return speed * time
d = find_distance(speed=10, time=3)    # like this. this is readable. This is called KEYWORD ARGUMENTS.
print(d)

d = find_distance(time=3, speed=10)     # even if order is changed, no problem. This is called KEYWORD ARGUMENTS.
print(d)

d = find_distance(3,10)     # This is not the same as above (in this case, speed=3, time=10)
print(d)