"""
🙅‍♂️ Input Functions in python:- In Python, input functions are used to take input from the user during program execution. The most commonly 
used input function. This is particularly useful when you want to create interactive programs where the user can provide data during execution.

⭐ How input Function Works:
👉 The input function waits for the user to type something and then press Enter. It reads the input as a string and returns it.

👉 Example:
Prompting the user for their myname
name = input("enter your name: ")
Displaying the user's input
print("Hello, " + name + "!")

"""
#---------------------------------------------------------------------------------------------------------------------
# ⭐ Input Function – Add 2 Numbers
# 👉 A simple program that takes two numbers as input from the user and prints their sum.
# 1. Prompting the user for the first and second number
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# 2. Since input() returns a string, we need to convert it to an integer
num1 = int(num1)
num2 = int(num2)

# 3. Calculating the sum and display the result
sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)


#---------------------------------------------------------------------------------------------------------------------
# ⭐ Multiple Input from User & Handling different Data Types
# input from user to add two number and print result
x = input("Enter first number: ")
y = input("Enter second number: ")

# casting input numbers to int, to perform sum
print(f"Sum of {x} & {y} is {int(x) + int(y)}")


#---------------------------------------------------------------------------------------------------------------------
# 1. Input from user
name = input("Enter your name: ")
print(f"Welcome to {name}")

age = input("Enter you age: ")
print(f"I am {age} years old")


#---------------------------------------------------------------------------------------------------------------------
# 2. Input from user to add two number
# 1st method
a = input("Enter your first number: ")
b = input("Enter your second number: ")
print(f"Sum of {a} and {b} is {int(a) + int(b)}")

# 2nd Method
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
print(f"Sum of {x} and {y} is {x + y}")


#---------------------------------------------------------------------------------------------------------------------
"""
Practice Question 1:- Write a program to input student name and marks of 5 subjects and print name and percentage in output?
"""
print("12th class result")
student_name = input("Enter your name: ")
hindi_marks = int(input("Enter your hindi marks: "))
english_marks = int(input("Enter your english marks: "))
maths_marks = int(input("Enter your maths marks: "))
science_marks = int(input("Enter your science marks: "))
socialScience_marks = int(input("Enter your socialScience marks: "))

# Calculating your marks in percentages:
percentage = ((hindi_marks + english_marks + maths_marks + science_marks + socialScience_marks)/500)*100

# print student result
print(f"The result of {student_name} is {int(percentage)}%. Well done..!!")


#---------------------------------------------------------------------------------------------------------------------
"""
Practice Question 2:- Write a python program that collects multiple types of data (e.g., name, age, height and student status) from user 
input, stores them in a dictionary and then prints out the collected data?
"""
# Initializing a dictionary
user_data = {}

# input from user
user_data["name"] = input("Enter your name: ")
user_data["age"] = int(input("Enter your age: "))
user_data["height"] = float(input("Enter your height: "))
user_data["student"] = input("Are you a student (Yes/No): ")

# print the input from users
print(user_data)


