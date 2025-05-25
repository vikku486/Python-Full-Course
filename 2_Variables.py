"""
🙅‍♂️ Python Variables:- A variable in Python is a name that refers to a value stored in memory. You can think of it as a label for a container 
    holding data.
👉 A variable is the name given to a memory location. A value-holding Python variable is also known as an identifier.
👉 Since Python is an interpreted and dynamically typed language, it automatically determines the typeof a variable at runtime, so we do not need 
   to explicitly declare its type.
👉 Variable names must begin with a letter or an underscore, but they can be a group of both letters and digits.
👉 The name of the variable should be written in lowercase. Both Rahul and rahul are distinct variables.


✅ Key Features of Python Variables
👉 No need to declare types (Python is dynamically typed).
👉 Value assigned determines the type.
👉 Variables are created when first assigned.
👉 Variable names are case-sensitive.


⭐ Identifier Naming:-
👉 The variable's first character must be an underscore or alphabet (_).
👉 Every one of the characters with-the-exception of the main person might be a letter set of lower-case(a-z), capitalized (A-Z), highlight, or 
   digit (0-9).
👉 White space and special characters (!, @, #, %, etc.) are not allowed in the identifier name. ^, &, *).
👉 Identifier name should not be like any watchword characterized in the language.
👉 Names of identifiers are case-sensitive; for instance, my name, and MyName isn't something very similar.
👉 Examples of valid identifiers: a123, _n, n_9, etc.
👉 Examples of invalid identifiers: 1a, n%4, n 9, etc.

"""


#---------------------------------------------------------------------------------------------------------------------
# Create a variables
name = "Vikas"
marks = 89.65
print(name)
print(marks)

# Ways to declare a variable name
# pascal case
MyName = "Vikas"
# camel case
myName = "Vikas"
# flat case
myname = "Vikas"
# snake case
my_name = "Vikas"



#---------------------------------------------------------------------------------------------------------------------
# Dynamic Binding
a = 6
print(a)

a = "vikas"
print(a)

b, c, d = 1, 2, 3
print(b, c, d)



#-----------------------------------------------------------------------------------------------------------------
# User Input
YourName = input("Enter Your Name: ")
print("Your name is:", YourName)

yourAge = input("Enter Your Age: ")
print("Your Age is:", yourAge)


num1 = input("Enter Your firstname: ")
num2 = input("Enter Your lastname: ")
result1 = num1 + num2
print(result1)


num1 = int(input("Enter Your Age: "))
num2 = int(input("Enter Your phone Number: "))
result2 = num1 + num2
print(result2)


num1 = float(input("Enter Your math mark: "))
num2 = float(input("Enter Your science mark: "))
result3 = num1 + num2
print(result3)



#-------------------------------------------------------------------------------------------------------------------
# Example:-
name = input("Enter Your Name: ")
myClass = int(input("Enter Your Class: "))
mark1 = float(input("Enter Your Math Marks"))

print("My Name is:", name)
print("My Class is:", myClass)
print("My Math Marks:", mark1)


