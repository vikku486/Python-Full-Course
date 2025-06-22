"""
🙅‍♂️ Strings:- Python string is the collection of the characters surrounded by single quotes, double quotes, or triple
quotes. The computer does not understand the characters; internally, it stores manipulated character as the combination
of the 0's and 1's.
Each character is encoded in the ASCII or Unicode character. So we can say that Python strings are also called the
collection of Unicode characters.
"""

# 👉 Creating Strings
a = 'Hello'
b = "Hello"
print(a)
print(b)

c = "It's raining outside"
d = """Hello, I am a "Data Analyst" """
print(c)
print(d)


# -----------------------------------------------------------------------------------------------------------------
# ⭐ Formatted Strings:-
# A formatted string in Python is a way to insert variables or expressions inside a string. It allows you to format
# the output in a readable and controlled way.
# 👉 There are multiple ways to format strings in Python:
# 1. Old-style formating(% operator)
# 2. str.format() method
# 3. F-strings (formatted string literals)

# 👉 1. Old-style formating(% operator):- This approach uses the % operator and is similar to string formatting in
# languages like C.
# Syntax: "string % value"
name = "Vikas"
age = 28
print("My name is %s and i am %d years old." % (name, age))


# 👉 2. str.format() method:- In Python 3, the format() method is more powerful and flexible than the old-style %
# formatting.
# Syntax: "string {}".format(value)
name = "Vikas"
age = 28
print("My name is {0} and i am {1} years old.".format (name, age))
print("My name is {name} and i am {age} years old.".format (name="Akash", age=30))


# 👉 3. F-strings (formatted string literals):- In Python 3.6, F-strings are the most concise and efficient way to
# format strings. You prefix the string with an f or F, and variables or expressions are embedded directly within
# curly braces {}.
# Syntax: f"string {variable}"
name = "Vikas"
age = 28
print(f"My name is {name} and I am {age} years old.")
print(f"My age after 5 years will be {age + 5}")

# -------------------------------------------------------------------------------------------------------------------
# ⭐ Escape Characters:-
# Escape characters in Python are special characters used in strings to represent whitespace, symbols, or control
# characters that would otherwise be difficult to include. An escape character is a backslash \ followed by the
# character you want to insert.

print(" \'Hello Python\' ")                    # Single Quotes
print(" \"Hello Python\" ")                    # Double Quotes
print(" \"Hello, I'm 'Vikas Sagar'\" ")        # Single/Double Quotes

print("Hello\nWorld")                          # Next Line
print("Hello\tworld")                          # Tabs space


# ------------------------------------------------------------------------------------------------------------------
# ⭐ Strings Operators:-

# Operator                                          Description
# 👉 +                    Concatenation:- Adds Values on either side of the operator.
# 👉 *                    Repetition:- Creates new strings, concatenating multiple copies of the same string.
# 👉 []                   Slice:- Gives the character from the given index.
# 👉 [:]                  Range Slice:- Gives the characters from the given range.
# 👉 in                   Membership:- Return True if a character exists in the given string.
# 👉 not in               Membership:- Return True if a character does not exist in the given string.
# 👉 r/R                  Raw String:- Suppresses actual meaning of Escape characters.
# 👉 %                    Format:- Performs String formating.

a = "Hello"
b = "Python"

# 👉  Concatenation
print(a + b)

# 👉  Multiple copies
print(a*3, b*3)

# 👉 Slice
print(a[4])

# 👉 Range Slice
print(a[1:4])

# 👉 in membership
print("H" in a)

# 👉 not in membership
print("H" not in a)

# 👉 Raw String: Suppress the escape characters
print(r"Hello\nWorld")


# ------------------------------------------------------------------------------------------------------------------
# ⭐ String Indexing:-
# You can access individual characters in a string using their index. Python uses zero-based indexing, meaning the
# first character has an index of 0. Index: Position of the character.
# Syntax:- string[Index_Value]
# String Indexing – Positive Index
my_name = "Hello Python"
print(my_name[0])
print(my_name[4])
print(my_name[8])

# String Indexing – Negative Index
print(my_name[-1])
print(my_name[-6])
print(my_name[-10])

# ------------------------------------------------------------------------------------------------------------------
# ⭐ String Slicing:-
# Slicing in Python is a feature that enables accessing parts of the sequence. String slicing allows you to get
# subset of characters from a string using a specified range of indices.
# Syntax: string[start : end : step]

str1 = "Harry Potter And The Goblet Of Fire"
print(str1)
print(str1[0:15])
print(str1[5:25])
print(str1[:8])
print(str1[6:])
print(str1[-5:])
print(str1[::2])
a = "0123456789"
print(a[::2])
print(a[:7:2])
# for reverse
print(a[::-1])
print(str1[::-1])


# ------------------------------------------------------------------------------------------------------------------
# ⭐ String Methods 1:-
# 1. len():-  To find the length of the string
# 2. count():- To find the number of times a character is occurring
# 3. upper():- To convert each letter into upper case
# 4. lower():- To convert each letter into lower case
# 5. index():- To find the index of any character
# 6. capitalize():- To convert the first letter to capital
# 7. case fold():-  To convert a string into lower case
# 8. find():- To find a character in string
# 9. format():- To write variables inside a string
# 10. center():- It fills the given characters and centralizes a string

str1 = "Hello, I am a Data Analyst"
print(str1)
print(type(str1))

# 👉 1. len():-
print(len(str1))

# 👉 2. count():-
print(str1.count("a"))

# 👉 3. upper():-
print(str1.upper())

# 👉 4. lower():-
print(str1.lower())

# 👉 5. index():-
print(str1.index("l", 6, 25))

# 👉 6. capitalize():-
print(str1.capitalize())

# 👉 7. case fold():-
print(str1.casefold())

# 👉 8. find():-
print(str1.find("l", 0, 15))

# 👉 9. format():-
name = "Honney"
age = 28
b = "My name is {}, and my age is {}"
print(b.format(name, age))

# 👉 10. center():-
print(name.center(35, "*"))


# -------------------------------------------------------------------------------------------------------------------
# ⭐ String Methods 2:-
# 👉 1. isalnum:- Returns True if all characters in the string are alphanumeric.
# 👉 2. isalpha:- Returns True if all characters in the strings are in the alphabet.
# 👉 3. isdecimal:- Returns True if all characters in the strings are decimal.
# 👉 4. isdigit:- Returns True if all characters in the strings are digit.
# 👉 5. isnumeric:- Returns True if all characters in the strings are numeric.
# 👉 6. islower:- Converts a string into lower case.
# 👉 7. isupper:- Returns True if all characters in the strings are upper case.
# 👉 8. isspace:- Returns True if all characters in the strings are whitespaces.
# 👉 9. istitle:- Returns True if the string follows the rules of a title.

a = "hello"
b = "123hello"
c = "12345"
d = "HELLO"
e = " "
f = "Hello 123@"
g = "1.234"
h = "Harry Potter And The Goblet Of Fire"
# isalnum()
print(a, a.isalnum())
print(b, b.isalnum())
print(f, f.isalnum())
print(g, g.isalnum())
# isalpha()
print(a, a.isalpha())
print(b, b.isalpha())
# isdecimal()
print(a, a.isdecimal())
print(c, c.isdecimal())
# isdigit()
print(g, g.isdigit())
print(c, c.isdigit())
print(b, b.isdigit())
# isnumeric()
print(b, b.isnumeric())
print(c, c.isnumeric())
# islower()
print(a, a.islower())
print(d, d.islower())
# isupper()
print(a, a.isupper())
print(b, b.isupper())
print(d, d.isupper())
# isspace()
print(e, e.isspace())
print(f, f.isspace())
# istitle()
print(d, d.istitle())
print(f, f.istitle())
print(h, h.istitle())


# -------------------------------------------------------------------------------------------------------------------
# ⭐ String Methods 3:-
# 👉 1. endswith():- Returns true if the string ends with the specified value.
# 👉 2. startswith():- Returns true if the string starts with the specified value.
# 👉 3. swapcase():- Swaps cases, lower case becomes upper case and vice versa.
# 👉 4. strip():- Returns a trimmed version of the string.
# 👉 5. split():- Splits the string at the specified separator, and returns a list.
# 👉 6. ljust():- Returns a left justified version of the string.
# 👉 7. rjust():- Returns a right justified version of the string.
# 👉 8. replace():- Returns a string where a specified value is replaced with a specified value.
# 👉 9. rindex():- Searches the string for a specified  value and returns the last position of where it was found.
# 👉 10. rfind():- Searches the string for a specified value and returns the last position of where it was found.

str1 = "   Harry Potter And The Goblet Of Fire"
# 👉 1. endswith()
print(str1.endswith("e"))

# 👉 2. startswith()
print(str1.startswith("H"))

# 👉 3. swap case()
print(str1.swapcase())

# 👉 4. strip()
print(str1.strip())
print(str1.strip("*, "))

# 👉 5. split()
print(str1.split(" "))

# 👉 6. ljust()
print(str1.ljust(60, "*"))

# 👉 7. rjust()
print(str1.rjust(60, "*"))

# 👉 8. replace()
print(str1.replace("Harry Potter", "Vikas Sagar"))

# 👉 9. rindex()
print(str1.rindex("And"))

# 👉 10 rfind()
print(str1.rfind("Potter", 5, 25))


# -------------------------------------------------------------------------------------------------------------------
# ⭐ Practice Questions:-
# 1. Fibonacci series
a = 0
b = 1
n = int(input("Enter a number here: "))
if n == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
print("Thanks")

# 2. If number is prime or not
num = int(input("Enter a number here: "))
if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Number is not a prime number")
            break
    else:
        print("It is a prime number")
print("Thanks")


# 3. Check for Palindrome
num = int(input("Enter a number here: "))
temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev*10 + dig
    num = num // 10
if rev == temp:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


# 4. Write a program to separate the following string into coma(,) separate values.
a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
print(a.split("."))

# 5. Write a program to short strings alphabetically in python.
b = "hello"
print(sorted(b))

# 6. write a program to remove a given character from a string.
c = "Hello World"
print(c.replace("o", "v"))

# 7. Write a program to remove dot(.) from the following string
d = "F.R.I.E.N.D.S"
print(d.replace(".", ""))

# 8. Write a program to check the number of occurance of a substring in a string.
e = "she sells seashells on the sea shore"
print(e.count("se"))


# 9. Take an input from a user as a string then, reverse it.
a = input("Enter anything here: ")
print(a[::-1])

# 10. Write a program to check if a string contains only digits.
a = input("Enter anything here: ")
print(a.isdigit())

# 11. Write a program to find number of vowels in a string.
a = input("Enter anything here: ")
vowels = 0
for i in a:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or
            i == "U"):
        vowels += 1
print("The number of vowels in the following strings are", vowels)


