#Insert the desired greeting - "Hello World!"
print("Hello World!")

#Name a variable
quote = """Code as if the person who needs to maintain your code
is a psychopath who knows where you live.
    - John"""

#Utelize the named variable
print(quote)

#Create a bool statement
print(5>10)

#Establish the code type
print(type(quote))

#Create an input tab for "Name"
input("Insert you name here:")

#Create an Arithmic equasion
a = 5
b = 2
c = a+b
print("Addition is", c)

print("Module is", a%b)
print("Floor devision is", a//b)


#Creating a Comparison Operator
age = 16
requiredAge = 18
print(age>=requiredAge)

age = 18
requiredAge = 18
print(age>=requiredAge)


#Creating a Logical Operator 
x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

a = 5
b = 8
print(a>b or a<b)


#Using membership operators in Strings
name = 'pythonx'
print('x' in name)
print('s' in name)
print('x' not in name)


#Lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
# prints out 1,2,3
for x in mylist:
    print(x)

# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
# together with a format string, which contains normal text together with "argument specifiers", 
# special symbols like "%s" and "%d". Let's say you have a variable called "name" with your user 
# name in it, and you would then like to print(out a greeting to that user.)

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#   %s - String (or any object with a string representation, like numbers)
#   %d - Integers
#   %f - Floating point numbers
#   %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#   %x/%X - Integers in hex representation (lowercase/uppercase)


#Identity Operator
#Variable is 
num = 5
#That variable is stored in a particular memory address and can be found using:
print(id(num))

num1 = 5
num2 = 5
num3 = 6
print(id(num1))
print(id(num2))
print(id(num3))
print(num1 is num2)
print(num1 is num3)


#Walrus operator - :=
#Walrus combines the variable naming and the print command into one step instead of two
#was 
name = "Sam"
print(name)

#Walrus
print(name='Sam')


# Descision making in Python is called Conditionals
# "If" checks true or false
# only excecutes if the "If" statement is true 
age=int(input("Enter your age:"))
if age >=18:
    print("Congratulations, you are elegible to vote!")


#"If-else"
age=int(input("What year were you born?"))
if age>=2006:
    print("Oops, you are not old enough to use this sevice yet!")
else: 
    print("Congratulations! You meet our minimum age requirements to use our services!")

#Indentation & IndentationErrors
#Choose if you want to use tab or space for indentation and stick to it, don't keep switching!
#Your indent amounts must differ with each block of code!


#if-elif-else
#Used for multiple strings of conditions of true
#You can have one if and one else statement but can have multiple elif statemnts
marks=int(input("What was your final score?"))
if marks>=90:
    print("Grade - Excellent!")
elif marks<90 and marks>=75:
    print("Grade - First Class")
elif marks<75 and marks>=40:
    print("Grade - Average")
else:
    print("Grade - Fail")


#Nested if-else
#Placing an if-elis-else inside an if-elis-else
username=input("Insert your username:")
password=input("Insert your password:")
if username=="Dani":
    if password=="123456":
        print("Login Successfull")
    else:
        print("incorrect Password")
else:
    print("User not found")


#Traffic light example elif code
light=input("Which colour is the traffic light?")
if light=="Green":
    print("please keep going")
elif light=="Yellow":
    print("Please go slow")
else:
    print("Please stop!")

#Game score example using 3 users
user1=9
user2=4
user3=7
if(user1>user2) and (user1>user3):
    print("User 1 is the winner!")
elif(user2>user1) and (user2>user3):
    print("User 2 is the winnder!")
else:
    print("User 3 is the winner!")


#Import
#reusability: code that has already been produced and can be modified to your needs
#Modules: pre-written code with functionalities that can be added to your own code
#import module_name
#when a module is imported, it imports the entire thing, you won't always want it all, but only snipets
#from module_name import 'something'


#CPython has a functioning Math module that is efficient
import math
#ceil(x) - Returns the smallest integer greater than or equal to x
#floor(x) - Same as above but the largest number
#fabs(x) - returns the absolute value of x
#factorial(x) - returns the factorial of x
#fmod(x,y) - returns the remainder when x is devided by y
#log2(x) - returns the base-2 logarithm of x
#log10(x) - same as above but base-10
#pow(x,y) - returns x raised to the power of y
#sqrt(x) - returns the square root of x
#trunc(x) - returns the truncated integer value of x

#The longer list of Python Math modules can be found on the python.org site


import math
print(math.sqrt(4))
print(math.fabs(-5))
print(math.floor(4.6))
print(math.pow(2,2))
print(math.trunc(7.999))

#to use any function or variable from a module we use the syntax
#module_name.function()


#Triganometry in Python
#Used mainly for scientific calculations
    #sin(x) - Returns the sine of x in radians
    #cos(x) - returns the cosine of x in radians
    #tan(x) - returns the tangent of x in radius
#Angle conversion functions to convert angles from degrees to radians and vice versa
    #degrees() - converts angle x from radians to degrees
    #radians() - converts angle x from degrees to radians
import math
print(math.sin(0))
print(math.sin(3))
print(math.cos(3))
print(math.tan(3))


#Mathimatical Constants
    #a key number whose value is fixed by an unambiguous definition, often refered to by a symbol.
    #Pi - 
print(math.pi)
    #Tau - 
print(math.tau)
    #Euler's number - 
print(math.e)
    #Infinity -
print("positive infinity-",math.inf)
print("negative infinity-",-math.inf)

#Code example to find the area of a cricle
import math
radius=int(input("Enter the radius of the circle"))
area=math.pi*radius*radius
print("Area of the circle is:", area)


#Random Module
    #seed(x) - initialize the random number generation
    #randrange(x,y,step) - return a random number between a given range
        #Steps value is the amount of numbers that will be skipped. between 1 and 10 and a step of 3, 
        #only the numbers 1, 4 and 7 can be generated
    #randint(x,y) - random number between the given range
    #choice(sequence) - random element from a given sequence
    #shuffle(sequence) - returns the sequence in a random order
    #random() - random float number between 0 and 1
#find more in Random Module on python.org
import random
print(random.random())
print(random.randint(1,100))
print(random.randrange(1,10))
print(random.randrange(1,10,2))


#A simple game example
#Guess the number
import random
generatedNumber=random.randrange(1,10)
userGuess=int(input("Guess a number in the range 1 through 10: "))
if userGuess==generatedNumber:
    print("You did it!")
elif userGuess < generatedNumber:
    print("Your guess is too low!")
else:
    print("Your guess is too high")



#Strings: sequesnce of characters in '' or ""

#String Formatting
#Having received user input and using the details from the input "Hello, Dani." instead of "Hello, User."
username=input("Please enter your name:")
print("Hello,",username)

#format() is used for positional formatting and the placeholder is defined using the {}
#be aware of your spaces (formatting) as the exact string will be used
name=input("What is your name?")
age=input("How old are you?")
print(("Hello, {}. You are {} years old.").format(name,age))


#fstrings- embed expressions within a string literals using minimal syntax
name=input("Enter your name:")
print(f"Hello, {name}!")
#inline artithmeticoperation
num1=5
num2=10
print(f"Five plus Ten is {num1+num2}")


#index - a numerical representation of an item's position in a sequence - always starts at 0
#variable_name[index_number]
appName="PythonX"
print(appName[0])
print(appName[2])


#Sclicing -obtaining a sub-string from the given stringby slicing it respectively from start to end
#string[start:end:step]

appName="PythonX"
print(appName[:4])
print(appName[2:5])
print(appName[3:])


#negative index - -1 gives the last element -2 thesecond last

#strings
    #Concatenation - combining two strings
        #using +operator
firstname="Dani"
lastname="Abel"
fullname=firstname+lastname
#add a space - fullname=firstname+" "+lastname
print(fullname)
        #using join() method - returns a string of which elements of the squence have been joined by the mentioned separator
firstname="Dani"
lastname="Abel"
print(" ".join([firstname,lastname]))
    #repetition - creating new strings byconcatenating multiple copiesof the same string
        # *
str="PythonX"
print(str*2)


#String built-in methods
    #capitalize()
    #count(X) -how many times does the variable appear
    #find(X)- search the string for a specific value, if it is not found it will be -1
    #index(X) - search for a specific value, if not found "error"
    #isalnum() - returns true if all the string characters are alphanumeric
    #isalpha() - returns true if all the string characters are in the alphabet
    #islower() - returns true if all the string characters are lowercase
    #isupper() - returns true if all the string characters are uppercase
    #join() - joins the elements of an iterable to the end of a string
    #lower() - converts a string into lowecase
    #replace(a,b) - returns a string when a value is replaced with b value
    #strip() - trimmed version of string - removes whitespaces from both ends
    #upper() - converts string into upper case
#all string methods return new values, and don't change they original string
str="PythonX"
print(str.islower())
print(str.isupper())
print(str.lower())
print(str.replace('P','A'))


#len() - accepts a string as a parameter & returns the length of the string
    #includes whitespaces
    #starts from 1
str="Love PythonX"


#Looping - repeat a particular task based on some conditions for some fixed number of times
    #For Loop - number of repeats are known
for i in range(5):
   print("PythonX")
# or
for i in "PythonX":
   print(i)
    #While Loop - number of repeats is unknown
        #WHILE BOOLEAN_EXPRESSION:
            #statement(s)
i=0
while i<3:
    print("I love Python")
    i=i+1

    #Break Statements - terminate the loop or statement in which it is present
str="Goodmorning"
for i in str:
    if i=="m":
        break
    else:
        print(i)
#Statements are followed in the order that they are written
#Sometimes we need a block of code to be repeated several times
    #Definite iteration - number is specified in advance
    #Indefinate iteration - repeats until conditions are met
#uses for val in sequence statements
    #val - variable that takes the value of the item inside the sequence each iteration
#Loop will continue until it reaches the last item in the sequence.
#The body of the loop is seperated from the rest of the code using indentation



#range(start,stop,step(optional)) - repeat an action a specific number of times
    #generate a sequence of numbers & is ommonly used for loop
print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,10,2)))


#Creating a multiplication table
#combine for-loop with range() to iterate 10 times
#the argument inside the range() function are (1,11) - starting from 1 and less than 11.
#Display the multiplication table of variable 'num
#in the print statement customize and format the output using the main logic num*i - which will give the result.
num=int(input('Enter the number of which you wish to generate the multiplication table:'))
for i in range(1,11):
    print(num, 'x',i,'=',num*i)


#Write a program that willprint even numbers in the specific range using a while-loop
#Accept input from the user for the specified range to generate even numbers
num=int(input("Enter the number up to which you want to generate even numbers:"))
i=0 
while i<=num:
    if i %2==0:
        print(i)
    i=i+1


#list - allows you to store a list of values to be accesed individually using index numbers
#a python data structure
    #ordered collections of multiple values
    #mutable - values can be changed and manipulated over a period of time
    #allows duplicate values
    #[integer, floatt, string, etc.]
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)
#an empty list
list1=[]

#list with values of same data type
list2=[1,4,6,3,9]

#list with values of different data types
list3=["John", 23, 56.4, True]

coursesEnrolled=["Python", "Ruby", "Java"]
print(coursesEnrolled)

#manipulating a lis:
    #accessing elements of a list
        #use indices - indexes are assigned from 0
names=["John", "Sam", "Berry", "Lin"]
print(names)
print(names[0])
print(names[3])
        #John = 0 Sam = 1 Lin = 3

    #List slicing
        #works the same as strings
names=["John", "Sam", "Berry", "Lin"]
print(names)
print(names[1:3])
print(names[2:])


    #Updating list
        #update value(s) over time
        #use operator (=)
marks=[56,76,69,71,39]
marks[4] = 43
print(marks)


    #deleting elements from a list
        #del statement
names=["John", "Sam", "Barry", "Lin"]
print(names)
del names[1]
print(names)
        #or to delete the entire list
del names


#much like with strings, lists have operation that can be preformed
    #Concatenation - adding two lists
        #'+' and "*"
list1=[1,2,3]
list2=[4,5,6]
print(list1+list2)

    #Repetition - below *3 means tht the same list is repeated 3 times, not times by 3
print(list1*3)     

    #Membership - gives True or False 
        # used to check the presence of a variable
        # (in) operator
enrolledList=["Sam", "Mike", "Kane", "Nick"]
print("Sam" in enrolledList)
print("Samuel" in enrolledList)


#preforming iteration
    #anything that is a sequence type can be iterated - use the concept of loops to iterate over the sequence
fruits=["Apple", "Mango", "Cherry", "Banana"]
for i in fruits:
    print (i)  # (i) = individual 

#the output:
            #Apple
            #Mango
            #Cherry
            #Banana

#check if a particular element is in the list or not - find Mango
fruits=["Apple", "Mango", "Cherry", "Banana"]
found_mango = False
for i in fruits:
    if i == "Mango":
        found_mango = True
        break
if found_mango:
    print("Found Mango")
else:
    print("Mango not found")
#try to imagine each iteration of the for loop. The first time through
#the loop, the value of i is "Apple", thus "mango not found" is printed. 
#the second iteration, the value of i is "Mango", and then break out of the loop
#I'd suggest saving the print statement until after the loop is done, and declaring 
# a variable to store whether or not the mango was found

                    #   or
fruits = ["Apple", "Mango", "Cherry", "Banana"]
if "Mango" in fruits:
    print("Found Mango")
else:
    print("Mango not found")

#Built-in for List
    #len(list) - returns the length of the list
    #min(list) - returns the elements with the minimum value
    #max(lis) - returns the elements with the maximum value
numbers=[23 ,56, 78, 13, 98, 33]
print(len(numbers))
print(max(numbers))
print(min(numbers))


#List Methods
    #list.method()
        #append(element) - adds specified element to the end of the list
        #insert(index,element) - insert element as specific index
        #pop() - removes and returns the element from the list
        #remove(element) - removes specified element
        #reverse() - reverse the order of the list items
        #index(element) - returns the index of the first matched item
        #count(element) - returns how many times an element apprears in the list
names=["James", "Sam", "Nick"]
print(names)
names.append("Barry")
print(names)
names.insert(1, "Ron")
print(names)
names.remove("Nick")
print(names)


#List comprehension
#Create a list of even numbers at runtime:
#Long way to do it
even=[]
for x in range(1,11):
    if x%2==0:
        even.append(x)
print(even)


#better way
    #consists of these parts
        #output expression
        #input sequence
        #a variable representing a member of the input sequence
        #an optional predicate part
#using list comprehension:
even=[x for x in range(1,11)if x%2==0]
print(even)
            # x =output expression
            # range(1,11) = input sequence
            # x = verable
            #if x%2==0 = predicate part/condition
#not all parts are compulsory
str="Hello, list"
characterList=[x for x in str]
print(characterList)


#Tuple - Read-Only list 
    #values can not be changed
        #ordered collections of multiple values
        #immutable
        #allows storing multiple values
    #placing the sequence inside ()

#empty tuple
tuple1=()
#same-data type tuple
tuple2=(1,4,6,3,9)
#different data type tuple
tuple3=("John", 23, 56.4, True)

#Example
    #You have an employee manageent website - 
    #you want to store the birth year of each employee to a specific department
employees=(1984, 1995, 1998, 1976)
print(employees)

#Manipulating Tuple
    #Accessin the elements of the Tuple
languages=("Python", "Java", "Ruby", "Lisp")
print(languages)
print(languages[0])
    #Tuple Slicing
print(languages[1:4])
    #Updating Tuple (not possible)
    #Deleting elements of Tuple
tuple=(12,56,98)
print(tuple)
del tuple

#Tuple Concatenation & Repetition
    #'+'and '*'
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1+tuple2)
print(tuple1*3)

#Tuple Memberships
names=("Sam", "Mike", "Kane", "Nick")
print("Sam" in names)
print("Samuel" in names)

#Tuple Built-in Functions
    #len(tuple) - returns length of tuple
    #min(tuple) - returns the elements of tuple with min value
    #max(tuple) - returns max value of tuple
numbers=(3,56,78,13,98,33)
print(len(numbers))
print(min(numbers))
print(max(numbers))
    #index(element) - returns index of first matched item
    #count(element) - how many times the element occurs in tuple
example=(23,45,23,67,89,1)
print(example.count(23))
print(example.index(67))

#Why Tuples?
    #Store multiple values & preform multiple operations
    #Advantage of Tuple vs List
        #Used for heterogeneous (different) data types
        #Since immutable - iterating is faster - preformance boost
        #Can be used as key for dictionaries since immutable
        #If you have data that doesn't change, tuples guarantee write-protect



#Dictionary - Key = words & Value=descriptions
    #Storing key-value pairs
        #Unordered & mutable collection of items
        #each item has key/value pair
        #Retrieve values when key is known
        #keys are unique/ values may be repeated
    #Created by ':' & items seperated by ',' enclosed in {}
dict2={1:"John", 2:"Sam"}
    #empty dictionary without items uses {}
dict1={}

#Example
studentsEnrolled={
    "John":"Python",
    "Sam":"Java",
    "Nick":["Python", "JavaScript"],
}
print(studentsEnrolled)

#Manipulating Dictionaries
    #Since dictionaries are unordered indexes cannot be used
    #Instead keys are used - since uniques
        #Accessing elements of dictionary
            #[] or get()
                #{} = Key Error if not found 
                # get() returns "None"
example={1:"John", 2:"Nick"}
print(example[1])
print(example.get(2))
        #Updating dictionary
example={1:"John", 2:"Nick"}
example[1]="Den"  #Changed
example[3]="Sim"   #Added
print(example)
        #Deleting element of dictionary
example={1:"John", 2:"Nick"}
del example[1]

#Dictionary Functions
    #keys() - returns list of dictionary keys
    #values() - list of dictionary values
    #clear() - removes all elements of a dictionary
    #get(key) - returns value of specified key or None
    #items() - returns list of dictionary key-value pairs in tuple form
empData={101:"Bravo", 102:"Asten", 103:"Kerry"}
print(empData.keys())
print(empData.values())
print(empData.items())
    #update(dict) - adds key-value pairs
empData={101:"Bravo", 102:"Asten", 103:"Kerry"}
empData.update({104:"Curan",105:"Elly"})
print(empData)
                #or
varDict={"Asia":["India","UAE","China"]}
varDict["Asia"].append("Japan")
print(varDict)
varDict["Asia"].remove("China")
print(varDict)

#iterating over a dictionary
empData={101:"Bravo", 102:"Sten"}
for i in empData:
    print(i)            #only prints key

for i in empData.values():
    print(i)            #only prints value

for i in empData.items():
    print(i)



#Sets
    #grouping objects
    #Can be distinguished by the unique opertions that canb be preformed
        #Sets are unordered collections - no index
        #Set elements are unique - no duplicates allowed
        #Sets can be muted but contained elements are immutable
    #set() or {}
data=set()
print(type(data))
    #sets may not have Lists or Dictionares in it
set1={1,2,3}
set2={6,7,8,"James"}
print(set1)
print(set2)

#Accessing elements of Sets
days={"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(days)

for day in days:
    print(day)          #prints the below eachother without any "" or {}

#Preforming set-specific operations
    #Union of sets
        #uses | operator or union()
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B)
print(A.union(B))           #neither repeats duplicate elements

#Set intersection is where the elements of A and B are the same/duplicate
    # & and intersection() operators
print(A&B)
print(A.intersection(B))        #only prints duplicates

#Set intersection
    #Difference of sets
#Set diffirence 
    #elements that are unique to A or B
        # difference() operator or "-"
print("A-B=", A-B)
print("A-B=", A.difference(B))

#Set built-in functions
    #len() - length aka number of elements
    # max()
    # min()
age={23,22,34,36,24,41}
print(len(age))
print(min(age))
print(max(age))
    # sorted() - re-shuffles set
    # sum() - sum of all elements

#Set Methods 
#  works as set.method()
    #add() - adds an element to the set
    #intersection() - returns the intersection of 2 sets as a new set
    #clear() - removes all elements
    #copy() - returns copy of set
    #discard() - removes and element if it is a member - gives error if not member
    #isdisjoint() - True if 2 sets have a null intersection
    #issubset() - True if another set contains this set
    #pop() - removes and returns any arbitrary set element
    #update() - updates the set with the union of itself and others
age.add(56)
age.remove(22)
age.pop()


#Functions - group similar tasks, can be reused & are excecuted only when called
    #reusability - important aspect of programming - rather than writing code again and again
    #Functions may take optional user input
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
num3=num1+num2
print("Addition is:", num3)

#Understanding the Structure of Function Syntax
    #def function_name(parameter1, parameter2...):
        #//block off code
        #return statement
#Functions: Key points
    #'def' is used to define a function
    #def is followed by functions in ()
    #function names can be anything
    #() may include optional input
    #: marks end of function reader
    #once function header is defined, the function body may contain 
        #multiple python statements
    #statements must be intended to make a block of code
    #optional return statement

#Calling function - won't excecute unless called
    #function_name() or function_name(parameter1, parameter2...)

#Defining a Function
def sayHello():
    print("Hello")

sayHello()      #call code

#Inserting more details
def sayHello(name):
    print("Hello", name)

sayHello("John")

#simple function
def addNumbers(num1, num2):
    num3=num1+num2
    return num3
print(addNumbers(5,6))

#Function Arguments & Parameters - information that can be passed into a function
    #Function Definition
def add(a,b):       #a,b is parameters
    return a+b
#function call
add(2,3)        #2,3 is arguments

def sayHello(name):
    print("hello", name)

sayHello("Mill")

            #or
def sayHello(name='User'):
    print("Hello,", name)

sayHello()



#Lambda - shortcut to define functions
    #they don't have a name
    #Useful in Django, Machine Learning, and Data Science
        #lambda arguments:expression
    #can take any number of arguments but only 1 expression
    #do not use a return keyword

lambda num1,num2:num1+num2

#calling a lambda function
add=lambda num1,num2:num1+num2
print(add(5,6))


#Files 
    #Named locations on disk to store related information
        #opening the file
            #open()
                #file_object=open(file_name, Access_mode)
            #modes
                #Read Mode -'r'
                    #"rb' read only in bionary format
                    # "r+" - both reading and writing
                    #'rb+' reading and writing in bionary format
                #Write Mode - content gets overwritten
                    #'w' write only
                    #'wb' write only in bionary
                    #'w+' write and read
                    #'wb+' write and read in bionary
                #Append Mode - content gets added at the bottom
                    #'a' opens file for appending
                    #'ab' bionary
                    #'a+' read and append
                    #'ab+' append and read bionary
        #preforming action (Reading or Writing)
            #print(fp.read())*** - opens content until it reaches the end of the file
            #read(size) - number of bytes to read from opened file - aka from start until where
            #readline() - single line of the file
            #readlines() - 
        #closing file
