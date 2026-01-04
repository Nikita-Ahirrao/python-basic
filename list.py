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

# To sort a list, use sort()
courses.sort()         # this should give error, read below. you can comment it if you don't want to see the red mark
print(courses)