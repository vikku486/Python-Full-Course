"""
🙅‍♂️ Loops:- A loop means to repeat something in then exact same way. Loops enable you to perform repetitive tasks
efficiently without writing redundant code. They iterate over a sequence (like a list, tuple, string, or range) or
execute a block of code as long as a specific condition is met.

⭐ Types of loop:-
👉 1. While Loop:- Repeats a statement or group of statements while a given condition is TRUE. It tests the condition
before executing the loop body.
👉 2. for Loop:- This type of loop executes a code block multiple times and abbreviates the code that manages the
loop variable.
👉 3. Nested Loop:- We can iterate a loop inside another loop.

⭐ Loop Control Statements:-
👉 1. Pass statement:- The pass statement is used when a statement is syntactically necessary, but no code is to be
executed.
👉 2. Break statement:- This command terminates the loop's execution and transfers the program's control to the
statement next to the loop.
👉 3. Continue statement:- This command skips the current iteration of the loop. The statements following the
continue statement are not executed once the Python interpreter reaches the continue statement.
"""

#--------------------------------------------------------------------------------------------------------------------
# ⭐ 1. While Loop:- The while loop repeatedly executes a block of code as long as a given condition remains True.
# It checks the condition before each iteration.
# Syntax:
# while condition:
#     Code block to execute

# Example1:- print numbers 1 to 5 using while loop?
i = 0
while i <= 5:
    print(i)
    i += 1


# 👉 else Statement: An else clause can be added to loops. It executes after the loop finishes normally (i.e., not
# terminated by break).

# Example2:- print numbers 5 to 1 with the help of while loop using else statements?
i = 5
while i > 0:
    print(i)
    i -= 1
else:
    print("While Loop Ended..!")


#--------------------------------------------------------------------------------------------------------------------
# ⭐ 2. For Loop:- The for loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary,
# set, or string) and execute a block of code for each element in that sequence.
# Syntax:-
# for variable in sequence:
#       code block to execute

# Example1:- Print the iterate over each character?
str1 = "Python"
for i in str1:
    print(i)

str2 = ("Vikas", "Akash", "Sagar")
for i in str2:
    print(i)

str3 = ["Apple", "Orange", "Banana"]
for i in str3:
    print(i)


# 👉 Using range() Function:- To repeat a block of code a specified number of times, we use the range() function.
# The range() function returns a sequence of numbers, starting from 0 by default, increments by 1 (by default),
# and stops before a specified number.
# 1. start: (optional) The beginning of the sequence. Defaults is 0. (inclusive)
# 2. stop: The end of the sequence (exclusive).
# 3. step: (optional) The difference between each number in the sequence. Defaults is 1.

# Syntax:-
# range(stop)
# range(start, stop)
# range(start, stop, step)

# Example1:- print numbers 1 to 10 with the help of for loop using range function?
for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)

# Example2:- Print the table 5 with the help of for loop using range function?
# 1st method:-
for i in range(1, 11):
    print("5 X", i, "*" " =", 5 * i)

# 2nd method:-
for i in range(1, 11):
    print(f"5 X {i} * = {5 * i}")
    

# ⭐ else Statement: An else clause can be added to loops. It executes after the loop finishes normally (i.e., not
# terminated by break).
for i in range(1, 11, 2):
    print(i)
else:
    print("For Loop Ended..!")


#-------------------------------------------------------------------------------------------------------------------
# ⭐ while loop  VS  for loop
# 👉 while loop:-
# 1. A while loop keeps running as long as a condition is true.
# 2. It is generally used when you don’t know how many iterations will be needed beforehand, and loop continues
# based on a condition.

# 👉 for loop:-
# 1. A for loop iterates over a sequence (like a strings, list, tuple, or range) and runs the loop for each item in
# that sequence.
# 2. It is used when you know in advance how many times you want to repeat a block of code.


#--------------------------------------------------------------------------------------------------------------------
# ⭐ 4. Nested Loop:- A loop inside a loop is called as nested loop. Nested loop are also used to solve pattern
# problems. Loop inside another loop is nested loop.

# 👉 Why Use Nested Loops?
# 1. Handling Multi-Dimensional Data: Such as matrices, grids, or lists of lists.
# 2. Complex Iterations: Operations depend on multiple variables or dimensions.
# 3. Pattern Generation: Creating patterns, such as in graphics or games.

# Syntax:
# Outer_loop:
    # inner_loop:
        #Code block to execute - inner loop
# Code block to execute - outer loop

# Example1:- Print numbers from 1 to 3, for 3 times using for-for nested loop?
for i in range(3):
    print("Outer loop iteration no, ", i)
    for num in range(1, 4):
        print(num)
print("Thank You..!")


# Example2:- Print numbers from 1 to 3, for 3 times using while loop for nested loop?
i = 1
while i < 4:
    print("while loop iteration no. ", i)
    for j in range(1, 4):
        print(j)
    i += 1


# Example3:- Print the triangle with using nested loop?
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
print("Thanks")


# Example4:- Print prime numbers from 2 to 10 using nested loop?
for num in range(2, 20):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)


#-------------------------------------------------------------------------------------------------------------------
# ⭐ Loop Control Statements:- Loop control statements allow you to alter the normal flow of a loop.
# Python supports 3 clauses within loops:
# 👉 1. Pass statement
# 👉 2. break statement
# 👉 3. continue statement


# ⭐ 1. Pass statement:- The pass statement is used as a placeholder (it does nothing) for the future code, and runs
# entire code without causing any syntax error. (already covered in functions).

# Example1:- Below example, the loop executes without error using pass statement.
for i in range(5):
# code to be updated
    pass

# Example2:-
count = 5
while count > 0:
    if count == 3:
        pass
    else:
        print(count)
    count -= 1


# ⭐ 2. break statement:- The break statement terminates the loop entirely, exiting from it immediately. or you can
# say that break statement is used when you want to destroy a loop at a certain condition and come out of the loop.

# Example1:- Below example, the loop terminated when condition met true for i == 3
for i in range(5):
    if i == 3:
        break
    print(i)


# Example2:-
for i in range(1, 6):
    if i == 4:
        break
    else:
        print(i)
print("Thank You!")


# ⭐ 3. continue statement:- The continue statement skips the current iteration and moves to the next one.
# Example1:- Below example, the loop skips when condition met true for i == 3
for i in range(5):
    if i == 3:
        continue
    print(i)


# Example2:-
for i in range(1, 6):
    if i == 5:
        continue
    else:
        print(i)


#--------------------------------------------------------------------------------------------------------------------
# 👉 Practice Question 1:- Write a program to find a sum of all the even numbers up to 50.
num = 0
for i in range(1, 51):
    if i % 2 == 0:
        num += i
print("The sum is even number up to 50 is: ", num)


# 👉 Practice Question 2:- Write a program to create pyramid triangle?
n = 5
for i in range(1, n+1):
    print(' ' * (n - i), end = "")
    print("*" * (2 * i - 1))


# 👉 Practice Question 3:- Write a program to write first 20 numbers and their squared numbers.
for i in range(1, 21):
    print(i * i)
print("Thanks")


# 👉 Practice Question 4:- Write a program to check if a number is divisible by 8 and 12, up to 100.
for i in range(1, 100):
    if i % 8 == 0 and i % 12 == 0:
        print(i)
print("Thanks")


# 👉 Practice Question 5:- Write a program to print a table
number = int(input("Enter your number: "))
i = 1
while i < 11:
    # print(number, "*", i, "=", number * i)
    print(f"{number} X {i} = {number * i}")
    i += 1


# 👉 Practice Question 6:- generate a casino game
import random
jackpot = random.randint(1,100)

guess = int(input("Do Guess Number"))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Wrong..! Please think higher")
    else:
        print("Wrong..! Please think lower")

    guess = int(input("Do Guess Number"))
    counter += 1
else:
    print("Correct guess")
    print("Attempts", counter)










