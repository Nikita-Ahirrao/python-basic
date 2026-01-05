#For Loop
# Use for loop to iterate through a list
courses = ['ba', 'bcom', 'bsc', 'be']

for course in courses:
    print(course)

# Use for loop to iterate through a tuple
fuits = ('apple', 'banana', 'mango')

for fruit in fuits:
    print(fruit)

# Use for loop to iterate through a dictionary
company = {'name': 'Tesla', 'founder':'Elon', 'year': 2003}

for item in company:
    print(item, company[item])

# Use for loop to iterate through a string
text = 'Hello'
for i in text:
  print(i)
  
# range() comes handy when using for loop

for i in range(5):   # prints from 0 to 4
  print(i)

print('------------')

for i in range(3,8):   # prints from 3 to 7
  print(i)  
  
# Use enumerator for getting index

courses = ['ba', 'bcom', 'bsc', 'be']
for id, item in enumerate(courses):
  print(id, item)  
  
# If you want index, but don't want to use enumerate, there is another way

courses = ['ba', 'bcom', 'bsc', 'be']

for i in range(len(courses)):                # range(5) prints a list of numbers from 0 to 4. Here we are passing length of list to the range.
  print(i, courses[i])  

# we can use condition inside for loop
courses = ['ba', 'bcom', 'bsc', 'be']

for course in courses:
    if course == 'bcom':
        print(course)
    else:
        print('Course is NOT bcom')

#break statement
# exit a loop at a certain condition, say 

courses = ['ba', 'bcom', 'bsc', 'be']
for item in courses:
  print(item)
  if item == 'bsc':                 # we wan't to break the loop when 'bsc' is reached
    break                           # 1. break is a special keyword that breaks through a loop  2. It is inside if statement, hence double identatition

# same as above, but let's print the values after if block. Just note the difference in output. 

courses = ['ba', 'bcom', 'bsc', 'be']
for item in courses:
  if item == 'bsc':                 # we wan't to break the loop when 'bsc' is reached
    break                           # 1. break is a special keyword that breaks through a loop  2. It is inside if statement, hence double identatition
  print(item)                       # In this case we are printing the item after checking the condition

#continue statement
# if item is 'bsc', stop the current iteration but continue with the next

courses = ['ba', 'bcom', 'bsc', 'be']
for course in courses:
  if course == 'bsc':
    continue
  print(course)
  
##
name = input('enter your name --- ')
print("let's print characeter separately")
for char in name:
  print(char)  
  
# Let's write a function that calculates square of each number
num = [1, 2, 3, 4, 5, 6, 7]

def sqr(item):
  return item * item

for i in num:
  print(i, sqr(i))  
  
# This gives the sum of the given list.

num = [10,30,23,43,65,12]  
sum = 0  
for i in num:  
    sum = sum + i     # or we can write sum += i
print("The sum is:",sum)  

# This gives multiplication table of number n given by user input

num = int(input("Enter the number "))  
for i in range(1,11):  
    c = num * i  
    print(f"{num} x {i} ====> {c}")   
    
# For loop inside for loop

adj = ["red", "big", "tasty"] #outer loop  
fruits = ["apple", "banana", "cherry"] #inner loop 

for x in adj:
  for y in fruits:
    print(x, y)

# NESTED loop

for i in range(4): # outer loop
    for j in range(20, 24): # inner loop
        print(i, j)

# Prints a pattern using astrisk symbol

rows = int(input("Enter the rows  :"))    # e.g. 3
for i in range(0, rows+1):               # Outer loop will print number of rows   (+1 because range excludes the second number)
    for j in range(i):                   # Inner loop will print number of Astrisk  
        print("*", end='')               # print() can take different arguments, by default end='\n' i.e. new line
    print()      
    
# Prints the number Pyramid

# User input for number of rows  
rows = int(input("Enter the rows : "))  
# Outer loop will print number of rows  
for i in range(0,rows+1):  
# Inner loop will print numbers 
    for j in range(i):  
        print(i, end = '')  
    print()  

# How to check length of list if there was no len() function

nums = [11,23,30,43]  
count = 0;  
for item in nums:  
    count = count + 1;
print("Total length - ",count);
            
# Check for some integer and print its index position using count identifier.
# Here we are trying to find position of 30

nums = [11,23,30,43]  
count = 0;  
for item in nums:  
    count = count + 1;
    if item == 30:  
        print("item matched")  
        break
print("found at", count, "location");

# If letter is 'c' then say 'Found letter' else print the letter

letters = ['a', 'b', 'c', 'd', 'e']
for letter in letters:
    if letter == 'c':
        print('Found letter')
        break
    else:
        print(letter)            
    