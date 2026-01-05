#Dictionaries are used to store data values in key:value pairs.
company = {
  "name": "Tesla",              # this is called dictionary iteam. This dictionary has 3 items. 
  "founder": 'Elon Musk',
  "established": 2003
}
print(company)
print(type(company))

# To access specific dictionary iteam, call it using its key 
print(company['name'])

# To get length of dictionary
print(len(company))    # 3 items

# To change value of an item, just override the value as follows
company['name'] = 'TESLAA'
print(company)

# Add new item in dictioary
company['location'] = 'US'
print(company)

#Dictionary Functions
print(company.get('name'))   # get() is predefined function for dict 
print(company.get('namee'))  # namee is not defined, so we get None

# keys() and values() functions gives us all the keys and  values
print(company.keys())
print(company.values())

# Let's add new key value pair to dictioary and see if we get the updated list with .key()
company['newkey'] = 'newval'
print(company.keys())
print(company.values())

# TO delete an item, use pop
student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}

print(student)
student.pop('class')    # use pop function and pass key
print(student)

# del can also be used to delete an item
student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}

print(student)
del student['class']     # syntax -> del dict_name['key']
print(student)

# clear() clears the dictionary without deleting the defined object. The dictionary just becomes empty (clear)
student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}

print(student)
student.clear()
print(student)

#Dictionary Looping
 #Let's first define dictionary in a different way
new = dict({'name': 'Apple', 'year': 1975, 'founder': 'Steve Jobs and Steve Wozniak'})     # dict is special keyword, wrap your dictionary within dict() 
print(new)
print(type(new))

# simple for loop
for item in new:              # this loops over only keys
  print(item)
  
for item in new:              # this loops over only keys
  print(item, new[item])      # for each key, let's access its value with new[keyname]  

# Shorter way to do the same is to use .items() function
for item, val in new.items():
  print(item, val)
        
# Loop through only values
for xyz in new.values():
  print(xyz) 
  
# You can sort dictionary 
for key in sorted(new):     # sorted() sorts all keys alphabetically
  print(key)     
  
#Nested Disctionary
company = {
    'name': 'Apple',
    'year': 1975,
    'founders': {
        'first': 'Steve Jobs',
        'second': 'Steve Wozniak'
    }
    }
print(company)
print(company['founders'])
print(company['founders']['first'])

for item, val in company.items():
  print(item, val)
  
print(type(company['founders']))  