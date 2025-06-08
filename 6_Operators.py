"""
🙅‍♂️ Python Operators:-
👉 Operators in python are special symbols or keywords used to perform operations on operands (variables and values).
1. Operators:- These are the special symbols/keywords. E.g., +, -, *, / etc.
2. Operands:- It is the value on which the operator is applied.
👉 In general, Operators are the symbols used to perform a specific operation on different values and variables.
These values and variables are considered as the Operands, on which the operator is applied. Operators serve as the
foundation upon which logic is constructed in a program in a particular programming language. In every programming
language, some operators perform several tasks.

⭐ Types of Operators in Python
Same as other languages, Python also has some operators, and these are given below -
1. Arithmetic Operators:- +, -, *, /, %, **, //
2. Comparison(Relational) Operators:- ==, !=, <=, >=, <, >
3. Assignment Operators:- =, +=, -=, *=, /=, %=, **=, //=
4. Logical Operators:- and, or, not
5. Bitwise Operators:- AND(&), OR(|), XOR(^), NOT(~), LEFT SHIFT(<<), RIGHT SHIFT(>>)
6. Membership Operators:- in, not in
7. Identity Operators:- is, is not
"""

#---------------------------------------------------------------------------------------------------------------------
"""
👉 1. Arithmetic Operators
Python Arithmetic Operators are used on two operands to perform basic mathematical operators like addition, 
subtraction, multiplication, and division. There are different types of arithmetic operators available in Python 
including the '+' operator for addition, '-' operator for subtraction, '*' for multiplication, '/' for division, 
'%' for modulus(remainder), '**' for exponent and '//' for floor division.
"""
a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % 2)
print( a ** 2)



#---------------------------------------------------------------------------------------------------------------------
"""
👉 2. Comparison Operators
Python Comparison operators are mainly used for the purpose of comparing two values or variables (operands) and return 
a Boolean value as either True or False accordingly. There are various types of comparison operators available in 
Python including the '==', '!=', '<=', '>=', '<', and '>'.
"""
a = 7
b = 5
print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)



#---------------------------------------------------------------------------------------------------------------------
"""
👉 3. Assignment Operators
Using the assignment operators, the right expression's value is assigned to the left operand. Python offers different 
assignment operators to assign values to the variable. These assignment operators include '=', '+=', '-=', '*=', '/=',
'%=', '//=', '**='.
"""
x = 10

x += 5                             # x = 10 + 5 → 15
print("x += 5:", x)

x -= 3                             # x = 15 - 3 → 12
print("x -= 3:", x)

x *= 2                             # x = 12 * 2 → 24
print("x *= 2:", x)

x /= 4                             # x = 24 / 4 → 6.0
print("x /= 4:", x)

x //= 2                            # x = 6.0 // 2 → 3.0
print("x //= 2:", x)

x %= 2                             # x = 3.0 % 2 → 1.0
print("x %= 2:", x)

x **= 3                            # x = 1.0 ** 3 → 1.0
print("x **= 3:", x)





#---------------------------------------------------------------------------------------------------------------------
"""
👉 4. Logical Operators
The assessment of expressions to make decisions typically uses logical operators. Python offers different types of 
logical operators such as and, or, and not. In the case of the logical AND, if the first one is 0, it does not depend 
upon the second one. In the case of the logical OR, if the first one is 1, it does not depend on the second one.

1. Logical AND: The condition will also be true if the expression is true. If the two expressions a and b are the same,
then a and b both must be true.
2. Logical OR: The condition will be true if one of the phrases is true. If a and b are the two expressions, then either
a or b must be true to make the condition true.
3. Logical NOT: If an expression a is true, then not (a) will be false and vice versa.

# Rules:-
1. True + True = True
2. True + False = False
3. False + False = False
"""

a = True
b = False
print(a and b)
print(a or b)
print(not a)



#---------------------------------------------------------------------------------------------------------------------
"""
👉 5. Bitwise Operators
The two operands' values are processed bit by bit by the bitwise operators. There are various Bitwise operators used 
in Python, such as bitwise OR (|), bitwise AND (&), bitwise XOR (^), negation (~), Left shift(<<), and Right shift(>>).

"""
a = 2                      # 0010
b = 3                      # 0011
print(a & b)               # 0010 & 0011 = 0010 → 2
print(a | b)               # 0010 | 0011 = 0011 → 3
print(a ^ b)               # 0010 ^ 0011 = 0001 → 1
print(~b)                  # ~0011 = -(3 + 1) = -4
print(a << b)              # 2 << 3 = 2 * 2^3 = 2 * 8 = 16
print(a >> b)              # 2 >> 3 = 2 // 2^3 = 2 // 8 = 0



#---------------------------------------------------------------------------------------------------------------------
"""
👉 6. Membership Operators:- We can verify the membership of a value inside a Python data structure using the Python membership 
operators. The result is said to be true if the value or variable is in the sequence (list, tuple, or dictionary); 
otherwise, it returns false.
1. in:- If the first operand (value or variable) is present in the second operand (sequence), it is evaluated to be 
true. Sequence can either be a list, tuple, or dictionary.
2. not in:- If the first operand (value or variable) is not present in the second operand (sequence), the evaluation 
is true. Sequence can either be a list, tuple, or dictionary
"""

print("D" in "Delhi")
print(1 in [2,3,4])
print("V" not in "Vikas")



#---------------------------------------------------------------------------------------------------------------------
"""
👉 7. Identity Operators:- Python offers two identity operators as is and is not, that are used to check if two values are 
located on the same part of the memory. Two variables that are equal do not imply that they are identical.

1. is:- If the references on both sides point to the same object, it is determined to be true
2. is not:- If the references on both sides do not point at the same object, it is determined to be true.
"""
a = ["Rose", "Lotus"]
b = ["Rose", "Lotus"]
c = a

print("a is c => ", a is c)
print("a is not c => ", a is not c)
print("a is b => ", a is b)
print("a is not b => ", a is not b)
print("a == b => ", a == b)
print("a != b => ", a != b)

































