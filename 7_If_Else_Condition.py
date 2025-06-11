"""
🙅‍♂️ Conditional Statements in Python:-
Conditional statements allow you to execute code based on condition evaluates to True or False. They are essential
for controlling the flow of a program and making decisions based on different inputs or conditions.
# Examples
a = 26
b = 108
if b > a:
    print("b is greater than a")
# Indentation - whitespace at the beginning of a line

⭐ Types of Conditional Statements
👉 There are 5 types of conditional statements in Python:
1. 'if' Statement
2. 'if-else' statement
3. 'if-elif-else' statement
4. Nested 'if-else' statement
5. Conditional Expressions(Ternary Operator):- Short hand statement and Short hand if statement


⭐ Statement                              Description
👉 If Statement             -> The if statement is used to test a specific condition. If the condition is true, a
                                block of code (if-block) will be executed.
👉 If-else Statement        -> The if-else statement is similar to if statement except the fact that, it also provides
                               the block of the code for the false case of the condition to be checked. If the condition
                               provided in the if statement is false, then the else statement will be executed.
👉 Nested if-else Statement -> Nested if statements enable us to use if ? else statement inside an outer if statement.
"""


#---------------------------------------------------------------------------------------------------------------------
# 👉 1. If Statement:- The if statement is used to test a condition and execute a block of code only if the condition
# is true.
# Syntax:
# if condition:
# Code to execute if the condition is true

# Example1:-
age = int(input("Enter your age: "))
if age >= 18:
    print("You are adult")
print("Thanks For your answer")



#---------------------------------------------------------------------------------------------------------------------
# 👉 2. If-else statement:- If else statement is used when you want to give two conditions to the computer. Here if
# one condition is false, program executes the another condition.
# Syntax:
# if condition:
# Code to execute if the condition is true
# else:
# Code to execute if the condition is false

# Example1:-
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")



#---------------------------------------------------------------------------------------------------------------------
# 👉 3. If-elif-else statement:- The if-elif-else statement allows to check multiple conditions and execute different
# blocks of code based on which condition is true.
# Syntax:
# if condition1:
# Code to execute if condition1 is true
# elif condition2:
# Code to execute if condition2 is true
# else:
# Code to execute if none of the above conditions are true

# Example1:-
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("You have A+ grade")
elif marks >= 80:
    print("You have A grade")
elif marks >= 70:
    print("You have B+ grade")
elif marks >= 60:
    print("You have B grade")
elif marks >= 50:
    print("You have C+ grade")
elif marks >= 40:
    print("You have C grade")
elif marks >= 33:
    print("You have D grade")
else:
    print("You are Fail")
print("Thank You")



#---------------------------------------------------------------------------------------------------------------------
# 👉 4. Nested 'if-else' statement:- A nested if-else statement in Python involves placing an if-else statement
# inside another if-else statement. This allows for more complex decision-making by checking multiple conditions that
# depend on each other.
# Syntax:
# if condition1:
    # Code block for condition1 being True
    # if condition2:
        # Code block for condition2 being True
    # else:
        # Code block for condition2 being False
# else:
    # Code block for condition1 being False

# Example1:-
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("You get a Android Phone")
    if marks >= 90:
        print("Or You get a iPhone")
        if marks >= 95:
            print("You get a Bike")
print("You have not anything buy")



# Example2:- Check positive, negative, even and odd number
number = int(input("Enter Your number: "))
if number > 0:
    if number % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")
else:
    if number == 0:
        print("This is zero")
    else:
        print("This is a negative number")



#---------------------------------------------------------------------------------------------------------------------
# 👉 5. Conditional Expressions:- Conditional expressions provide a shorthand way to write simple if-else statements.
# Also known as Ternary Operator.
# Syntax:
# value_if_true if_condition else value_if_false


# example1:- Short hand statement
marks = int(input("Enter your marks: "))
if marks >= 90: print("You will get a new phone")



# example2:- Short hand if statement
marks = int(input("Enter your marks: "))
status = "You will go to trip" if(marks >= 90) else "No phone for a month"
print(status)



#---------------------------------------------------------------------------------------------------------------------
# 👉 Practice Question1:- Write a program that prompts the user to enter a username and password and
# checks whether they match. Provide appropriate messages for the following.
# • Both username and password are correct.
# • Username is correct but password is incorrect.
# • Username is incorrect.

# Predefined username and password
predefined_email = "vikassagar486@gmail.com"
predefined_password = "12345"

# Prompt the user for username and password
email = input("Enter your email: ")
password = input("Enter your password: ")

# Check the username and password
if email == predefined_email and password == predefined_password:
    print("Welcome user")
elif email == predefined_email and password != predefined_password:
    print("Incorrect password")
    password = input("Enter your password again: ")
    if password == predefined_password:
        print("Welcome, user again")
    else:
        print("You are blocked")
else:
    print("Incorrect user")



# 👉 Practice Question2:- Write a program to find out minimum value.
a = int(input("Enter your first value: "))
b = int(input("Enter your second value: "))
c = int(input("Enter your third value: "))

if a < b and a < c:
    print("a is the smallest value")
elif b < c:
    print("b is the smallest value")
else:
    print("c is the smallest value")



# 👉 Practice Question3:- Leap Year Write a simple program to determine if a given year is a leap year using user input.
# Note:-
# • Leap year occurs once every four years.
# • A year is a leap year if it is divisible by 4, but not if it is divisible by 100 unless it is also divisible by 400.
# Every year that is exactly divisible by 4 is a leap year, except for years that are exactly divisible by 100, but
# these centurial years are leap years if they are exactly divisible by 400. For eg, the years 1700, 1800, & 1900 are
# not leap years, but the years 1600 and 2000 are.

# User_input
year = int(input("Enter a year (e.g. 2024): "))
# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")




























