#Arithmatic Operators
# Let's first define two numbers in a variable and print them and their type
num1 = 3
num2 = 5
print(num1, num2)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num2 / num1)
print(type(num1), type(num2))
print(3 ** 2)        # exponent (^) ---> 3^2

#Comparison Operators
# == checks whether left hand side and right hand side is equal

print(2 == 2)   # if LHS = RHS, output True else False
print(2 == 1)   # Here LHS is not equal to RHS
print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 3)
print(3 >= 2)
print(3 <= 2)

#Assignment Operator
# += is a shortcut for add and assign 
num = 4
print(num)
num += 1   # is equivalent to num = num + 1
print(num) 

# -= is a shortcut for subtract and assign
num = 4
print(num)
num -= 1   # is equivalent to num = num - 1
print(num) 
num = 4
num *= 2
print(num)
num = 4
num /= 2
print(num)

#Logical Operators
#Basics - 3 Operators - And, Or, Not
# Three cases of AND
print(True and True)
print(True and False)   # same as False and True
print(False & False)    # instead of and, you can use &
# In short, if any one is false then answer is false 

# Three cases of OR
print(True or True)   
print(True or False)
print(False | False)  
# In short, if any one is true then answer is true 

# not is opposite of something (bool)
print(not True)
print(not False)

x = 5
print(x > 4 and x < 6)   #AND
x = 5
print(x > 3 or x < 4)    #OR
x = 5
print(not(x > 3 and x < 10))   #NOT

#Some functions related to int and float
# abs() function gives positive number
print(abs(-2))
print(abs(-2.1))

# round() function rounds off the digits after decimal point
print(round(3.45))
print(round(-3.95))
print(round(3.46, 1))   # round the number till 1 decimal place
print(round(3.46, 2))   # round the number till 2 decimal place

#if you add string and integer, you'll get a string
num1 = 'Hello'
num2 = '5'
print(num1 + num2)

#Type casting Integers
#Basic Typecasting
# Type casting  i.e. converting string to int 
a='2'
b='3'
print(a,type(a))
print(b,type(b))
print('Addition',a+b)
print()
a=int(a)
b=int(b)
print(a,type(a))
print(b,type(b))
print('Addition',a+b)

a='2.0'
print(type(a))
a=str(a)
print(a,type(a))

a='True'
print(type(a))
a=bool(a)
print(type(a))

#Typecasting with input()
num = input('Enter Any Number : ')
print(num,type(num))

#n=int(num)
#print(n,type(n))

# Carry addition of two user-inputted numbers
num1 = input('Enter first number:  ')
num2 = input('Enter second number:  ')
print(num1 + num2)    # this will simply append the two numbers one after the other
print(int(num1) + int(num2))   # this will actuall carry out the addition 

#If Else based on comparison operators
x=100
y=20
if x<y :
    print("Y is greather Than X")
else:
    print("X is Lesser Then Y")  
      
#multiple if else => use elif
height = 176
if height < 140:
    print('too short')
elif height < 180:
    print('height is ok')
else:
    print('too tall')
    
# Nested If
x = 7
if x > 10:
    print('x is greater than 10')
    if x > 20:
        print('x is greater than 20')
        if x > 30:
            print('x is greater than 30')
        else:
            print('x is smaller than 30')
    else:
        print('x is smaller than 20')
else:
    print('x is smaller than 10')   
    
# To find out if inputted number is within the range of 3 to 10 
# if both conditions are True only then answer will be True else false

x = int(input("Enter any number within range 10: "))     # if you pass anything other than integer, it'll throw error. Because we are typecasting here itself
print(x >= 3 and x <= 10)    