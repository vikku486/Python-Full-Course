"""
🙅‍♂️ Type Casting:- Type casting in Python refers to converting the data type of a variable from one type to another. This can be done either 
explicitly by the programmer or implicitly by Python. This can be useful in various situations, such as when you need to perform operations 
between different types or when you need to format data in a specific way.

⭐ Python has several built-in functions for type casting:
👉 int():- Convert a value to an integer.
👉 float():- Converts a value to a floating point.
👉 str():- Converts a value to a string.
👉 list(), tuple(), set(), dict() and bool().


⭐ Implicit Type Casting:- Implicit Type Casting occurs when Python automatically converts one data type to another during an operation, 
without any explicit request from the programmer.
This usually happens when a lower data type is converted to a higher data type to prevent data loss.

⭐ Explicit Type Casting:- Explicit Type Casting is when you manually convert one data type to another using built-in Python functions. 
This is necessary when Python doesn't automatically convert types (unlike implicit casting).


"""


#---------------------------------------------------------------------------------------------------------------------
# Casting in Python
# 1. converts string into integer
a = 1
print(type(a))
b = "1"
print(type(b))
c = int(b)
print(type(c))
print(a + c)


#---------------------------------------------------------------------------------------------------------------------
# 2. converts float into integer
f1 = 22.56
f2 = int(f1)
print(f2)
print(type(f2))


#---------------------------------------------------------------------------------------------------------------------
# 3. converts integer into float
int1 = 26
f3 = float(int1)
print(type(f3))
print(f3)


#---------------------------------------------------------------------------------------------------------------------
# Implicit type casting
var1 = 10              #int type
var2 = 15.5            #float type
var3 = var1 + var2
print(var3)
print(type(var3))


#---------------------------------------------------------------------------------------------------------------------
# Explicit type casting
int_num = 101
str_num = str(int_num)
print(type(str_num))

c1 = bool(0)
print(c1)
print(type(c1))

c2 = bool(1)
print(c2)
print(type(c2))


















