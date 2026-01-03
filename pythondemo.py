print("Hello , My name is Nikita Ahirrao")
a = "Hello world!!"
print(a)

# Let's check the data type of variable 'dummy'
print(type(a))

# Let's explore other data type quickly before focusing our attention to strings
num1 = 5
num2 = 4.5
print(type(num1))
print(type(num2))
val = True
print(type(val))

 #Let's just print the actual values 
print(num1)
print(num2)
print(val)

#string basic 
str = 'I am Working in AI leela'
print(str)

#Use len() function to check length of the string
print(len(str))
#To print a character at specific position
text = 'Welcome to python !'
print(text[5])
print(text[-1])
print(text[5:10])
print(text[:2])
print(text[5:])
print(text[-4])
#prints string in uppercase and Lowercase
print(text.upper())
print(text.lower())
print(text.title())
#Use count() to check how many times a particular character is repeated in the text
print(text.count('p'))
print(text.count('to'))
print(text.find('o'))
print(text.find('z'))
# Let's replace a word by some other word
print(text.replace('python','java'))
# Replace function does not change our original text, instead it returns us a new string. So as you can see below, the original text is maintained as it was. 
print(text)

fruit = 'applllllleeeeeee'
print(fruit.replace('e','E'))
print(fruit.replace('z','E'))    # No change because 'z' does not exist in the original string
# strip() removes the blank spaces before and after the first and last character respectively 
msg = '   Hello World    '
print(msg)
print(msg.strip())
# The other way to cross check is to measure the number of blank spaces with count() function
print(msg.count(' '))
print(msg.strip().count(' '))

# The following string will be broken into a list of string whenever ',' is observed
address = '102, Dhiraj patil, Nandurbar'
print(address.split(','))
output = address.split(',')
print(output)
print(type(output))

# Connecting two strings together
first_name = 'Nikita'
last_name = 'Ahirrao'
name = first_name + last_name
print(name)
name = first_name + ' ' + last_name
print(name)
# {} is a special placeholder
name = '{}    {}'.format(first_name,last_name)
print(name)
# Yet another way to do the same (short and sweet)
# This is called 'f string'. Simply pass the variable name inside f'' within {}
name = f'{first_name}        {last_name}'
print(name)
name = f'{first_name.upper()} {last_name.lower()}'
print(name)

#Integer and float 
a = 4
b = 5
print(a,b)
print(type(a),type(b))
c=a+b
print(c)
#arithmatic operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(type(a/b))

#Just like integer, arithmatic operations can be applied on float
new1 = 2.4 
new2 = 3.1
print(new1+new2)
print(new1-new2)
# Float and integer can be added to each other
i=5
f=0.1

# Let's accept input from user
# input is a special function that allows user to type (and pass) user's own input
name = input("Enter your Name : ")
print(name)
print(type(name))

#gives two number from user and perfom arthmatic operation on that number
#menu driven program
num1 = float(input("enter first number  "))
num2 = float(input("enter second number  "))

while True:
    print("1.Addition ")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division ")
    print("5.module")
    print("6.exit")
    
    choice = int(input("Enter your choice : "))
    if choice==1 :
        print("Addition : ",num1+num2)
        
    elif choice==2 :
        print("subtraction ", num1-num2)
        
    elif choice==3 :
            print("multiplication ", num1*num2)
            
    elif choice==4 :
        if num2!=0 :
            print("Division ", num1/num2)
        else :
            print("error : cannot divided by zero")    
              
    elif choice==5 :
        print("module ", num1%num2) 
        
    elif choice == 6 :
        print("exit !!")
        break
    else:
        print("Invalid Choice !")      
        
          
    
