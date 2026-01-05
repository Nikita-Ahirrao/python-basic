#Conditional Statements 
#if
a = 33
b = 200
if b > a:
  print("b is greater than a")

# We can find the number is even or odd.

n = int(input(" Enter a number to check:"))

if n % 2 == 0:
  print("It's an even number.")
if n % 2 != 0:
  print("It's an odd number.")
if n == 0:
  print("The number is neither even nor odd. Rather you entered Zero.")

# Using If statement, we can find largest number among the

a = int(input("Enter the Value of a: "));  
b = int(input("Enter the Value of b: "));  
c = int(input("Enter the Value of c: "));  

if a>b and a>c:  
    print("a is largest input.");  
if b>a and b>c:  
    print("b is largest input.");  
if c>a and c>b:  
    print("c is largest input.");  

#If Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
age = int (input("Enter your age? "))  
if age>=18:  
    print("You are eligible to vote !!");  
else:  
    print("Sorry! you have to wait !!"); 
    
#if Elif Else
x = 3
if x == 1:
  print('x is one')
elif x == 2:
  print('x is two')
elif x == 3:
  print('x is three')
else:
  print('x not found')

# Check whether the inptted number is 30, 40 or 50. 

number = int(input("Enter the number?  "))  

if number==30:  
    print("The number you entered is: 30 ")  
elif number==40:  
    print("The number you entered is: 40") 
elif number==50:  
    print("The number you entered is: 50")
else:  
    print(" You have entered a random number other than 30, 40 and 50.")  
##

marks = int(input("Enter the marks? "))  

if marks > 85 and marks <= 100:  
   print("Congrats ! you scored grade A ...")  
elif marks > 60 and marks <= 85:  
   print("You scored grade B + ...")  
elif marks > 40 and marks <= 60:  
   print("You scored grade B ...")  
elif (marks > 30 and marks <= 40):  
   print("You scored grade C ...")  
else:  
   print("Sorry you are fail !!")  

#Nested IF
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#Shortcut to write if-else when the if-else code block is single line
# If you have only one statement to execute, you can put it on the same line as the if statement.

if a > b: print("a is greater than b")

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 2
b = 330
print("A") if a > b else print("B")


