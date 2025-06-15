"""
🙅‍♂️ Functions in Python:-
A function is a block of code that performs a specific task. You can use it whenever you want by calling its name,
which saves you from writing the same code multiple times.
👉 Benefits of Using Function:  Increases code Readability & Reusability.

⭐ Basic Concepts:-
👉 1. Create function:- Use the "def" keyword to define a function.
👉 2. Call function:- Use the function's name followed by () to run it.
👉 3. Parameter:- The variable listed inside parentheses in function definition.
👉 4. Argument:- The actual value you pass to function when you call it.

⭐ Types of Functions:-
👉 Below are the two types of functions in Python:-
1. Built-in library function:
    * These are Standard functions in Python that are available to use.
    * Examples: print(), input(), type(), sum(), max(), etc.
2. User-defined function:
    * We can create our own functions based on our requirements.
    * Examples:  create your own function :)

👉 Syntax:-
def my_function(parameter):
    instruction-1
    instruction-2
return result
# return result is optional, Use if you want the function to give back a value.
"""


#--------------------------------------------------------------------------------------------------------------------
# 👉 1. Function without Parameters
# Example1:- Create or Define Function
def greetings():
    print("Welcome to Python")
# Use or call this Function
greetings()




#--------------------------------------------------------------------------------------------------------------------
# 👉 2. Function with Parameters
# Example2:- function to adds two numbers & print result.
def add2numbers(a, b):
    result = a + b
    print("The sum is:", result)
# Calling this function with arguments
add2numbers(5, 3)




#--------------------------------------------------------------------------------------------------------------------
# 👉 3. The return Statement:- The return statement is used in a function to send a result back to the place where
# the function was called. When return is executed, the function stops running and immediately returns the specified
# value.
# Example3:-
def add(a, b):
    return a + b      # This line sends back sum of a and b
result = add(10, 5)
print(result)



# Example4:- function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# Calling this function to return a value
temp_f = celsius_to_fahrenheit(25)
print("Temperature in Fahrenheit:", temp_f)




#-------------------------------------------------------------------------------------------------------------------
# 👉 4. The pass Statement:- The pass statement is a placeholder in a function or loop. It does nothing and is used
# when you need to write code that will be added later or to define an empty function.
# Example5:-
def myfunction():
    pass  #This does nothing for now



#--------------------------------------------------------------------------------------------------------------------
# 👉 Practice_Question1:- Write a program to create a simple calculator?
# Steps to build calculator program:-
# 1. Functions for operations
# 2. user input
# 3. print result

# Step1:- Create functions:-
# Function to add two numbers
def add(num1, num2):
    return num1 + num2
# Function to sub two numbers
def sub(num1, num2):
    return num1 - num2
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
# Function to average two numbers
def avg(num1, num2):
    return (num1 + num2)/2

# Step2:- user input
print("Please select a operation:\n" "1. Addition\n" "2. Subtraction\n" "3. Multiply\n" "4. Division\n" "5.Average\n")
select = int(input("Select a operation from 1,2,3,4,5: "))
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Step3:- Print the result
if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))
elif select == 2:
    print(number1, "-", number2, "=", sub(number1, number2))
elif select == 3:
    print(number1, "*", number2, "=", multiply(number1, number2))
elif select == 4:
    print(number1, "/", number2, "=", divide(number1, number2))
elif select == 5:
    print("(", number1, "+", number2, ")", "/", "2", "=", avg(number1, number2))
else:
    print("Invalid operation! Please select again")
print("Thank You so much..!")




#--------------------------------------------------------------------------------------------------------------------
# 🌟 Arguments in Function:- Arguments are the values that are passed into a function when it’s called. A function
# must be called with the right number of arguments. If a function has 2 parameters, you must provide 2 arguments
# when calling it.
#
# 👉 Example: function defined using one parameter (variable)
def greetings(name):   # name is a parameter
    print("Hello, " + name + "!")
greetings("Vikas")     # Vikas as argument
# Output: Hello, Vikas!



# ⭐ Types of Function Arguments:- Python supports various types of arguments that can be passed at the time of the
# function call.
# 👉 1. Required arguments (Single/Multiple arguments)
# 👉 2. Default argument
# 👉 3. Keyword arguments (named arguments)
# 👉 4. Arbitrary arguments (variable-length arguments *args and **kwargs)



#---------------------------------------------------------------------------------------------------------------------
# 👉 1. Required Arguments(Single/Multiple arguments):- Required arguments are the arguments passed to a function in
# correct positional order. A function must be called with the right number of arguments. If a function has two
# parameters, you must provide 2 arguments when calling it.

# Example: function defined using one parameter (variable)
def greeting(name, age):                       # parameter
    print("Hello, My name is", name, "my age is", age, "years old.!")
greeting("Vikas", 28)                # arguments



#---------------------------------------------------------------------------------------------------------------------
# 👉 2. Default Arguments:- You can assign default values to arguments in a function definition. If a value isn't
# provided when the function is called, the default value is used.

# Example: function defined using one parameter & default value.
def greeting(name = "Vikas"):
    print("Hello", name)
greeting()
greeting("Akash")




#---------------------------------------------------------------------------------------------------------------------
# 👉 3. Keyword Arguments:- When calling a function, you can specify arguments by the parameter name. These are called
# keyword arguments and can be given in any order.

# Example: function defined using two parameters
def divide(a, b):
    return a / b

result1 = divide(100, 20)       # position argument
print(result1)

result2 = divide(a = 10, b = 100)     # keyword(named) argument
print(result2)




#---------------------------------------------------------------------------------------------------------------------
# 👉 4(a). Arbitrary Positional Arguments (*args):- If you're unsure how many arguments will be passed, use *args to
# accept any number of positional arguments.
# 1. Purpose: Allows you to pass a variable number of positional arguments.
# 2. Type: The arguments are stored as a tuple.
# 3. Usage: Use when you want to pass multiple values that are accessed by position.
# Notes:- Here, *args collects all the passed arguments into a tuple and sum() function adds them.

# Example1:-
def add_numbers(*args):
    return sum(args)

result = add_numbers(10, 10, 15, 25, 40)      # variable number of arguments
print(result)



# Example2:-
def greeting(*names):
    for name in names:
        print(f"Hello, {name}!")

greeting("Vikas", "Honey", "Akash")




#---------------------------------------------------------------------------------------------------------------------
# 👉 4(b). Arbitrary Keyword Arguments (**kwargs):- If you want to pass a variable number of keyword arguments, use
# **kwargs.
# 1. Purpose: Allows you to pass a variable number of keyword arguments (arguments with names).
# 2. Type: The arguments are stored as a dictionary.
# 3. Usage: Use when you want to pass multiple values that are accessed by name.
# Note:- Here, **kwargs takes in any number of keyword arguments and prints each key-value

# Example:-
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Vikas", age=28, position="Data Analyst")



#-------------------------------------------------------------------------------------------------------------------
# 🙅‍♂️ Lambda Function in Python:- A Lambda function in python is a small, anonymous function defined using the lambda
# keyword. It can have any number of arguments, but only one expression, which is evaluated and returned.
# Lambda functions are often used for short, simple operations without needing to define a full function using def.

# 👉 Syntax:-
# lambda arguments: expression

# * Arguments: Input to the function.
# * Expression: A single statement or operation that the lambda function

# ⭐ Lambda function example:-
# 👉 1. Add two numbers using a regular function:
def add(x, y):
    return x + y
print(add(3, 5))    #output 8


# 👉 2. Add two numbers using a lambda function:
add = lambda x, y: x + y
print(add(3, 5))   #output 8


# 👉 3. Custom Sorting - Sort a list of tuples by the second elements:
data = [(1, "b"), (3, "a"), (2, "c")]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)      #output [(3, "a"), (1, "b), (2, "c")]






