#Collection Data Type
#list
# Define a list
courses = ['ba', 'bcom', 'bsc', 'ma', 'mcom', 'msc']
print(courses)         # Note that the output is in square bracket. Remember, square brackets denote list
print(type(courses))

#Accessing List items
print(courses[0])
print(courses[3])
print(courses[0:2])
print(courses[-1])
print(courses[-3:-1])
print(courses[-2:])

#List functions
#To insert an element somewhere in the middle, say 3rd index
courses.insert(3, 'ME')           # i.e. insert requires position and value
print(courses)

# You can append another variable as well
c = 'B.Pharm'
courses.append(c)
print(courses)

# You can append a list within a list
new = ['11th', '12th']   # Defining a new list
courses.append(new)      # Appending new list to the old list
print(courses)           # Note that the list itself got inserted into the list. That list constitutes one element and not two. 

courses.extend(new)
print(courses)

# To remove last entry of list, use pop()
courses.pop()
print(courses)
# To remove specific item, use remove()
courses.remove('ba')
print(courses)    # ba is removed

# Let's define new list
fruits = ['mango', 'apple', 'orange', 'kiwi', 'pineapple', 'papaya']
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

# Similary, sort works on the list with only numbers as well
nums = [12, 4, 2, 11, 1, 100]
print(nums)
nums.sort()
print(nums)

#functions that can be used with List
countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']
print(len(countries))

nums = [8, 4, 2, 1, 16]     # Returns the highest number, when list is of numbers
print(max(nums))
print(min(nums))
print(sum(nums))

#Iterating a list
countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']
#Let's define a simple for loop

for item in countries:            # item could be changed by any other random name. 
  print(item)
  
# Let's spice up the things little bit

for item in countries:
  print(item, len(item))
  
for item in countries:
      print(f'{item} --- {item.upper()} --- {len(item)}')  # f string allows to easily combine our print strings and python codes  

for item in countries:
  print(f'{item} --- {item.upper()} --- {len(item)}')  # f string allows to easily combine our print strings and python codes
  
# let's try to create a list using for loop and append()
cubes = []    # first define a blank list
for i in range(5):       # you can explore what range(5) gives. In short, it returns numbers upto 5. 
  cubes.append(i ** 3)
print(cubes)  

# To deconstruct what is exactly happening in the above code, you can use print() like this

cubes = []    
for i in range(5):       
  print("i = ", i)
  cubes.append(i ** 3)
  print("Number appended (i ** 3) = ", i ** 3)
  print("Current status of cubes list = ", cubes)
print()
print('Outside for loop')
print(cubes)

#Nested list
fruits = [['mango','apple','pineapple'], ['sitafal', 'orange']]
print(fruits)
print(len(fruits))
print(fruits[0], type(fruits[0]))
print(fruits[1], type(fruits[1]))
print(fruits[0][0])
print(fruits[1][0])
print(fruits[0][2])