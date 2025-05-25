"""
🙅‍♂️ Python Data Types:- Python Data types are the classification or categorization of data items. It represents the kind of value that tells 
what operations can be performed on a particular data. Since everything is an object in Python programming, Python data types are classes and 
variables are instances (objects) of these classes.
👉 In Python, A data type is a classification that specifies the "type of value" a variable can hold. We can check data type using 
"type()" function.
👉 Every value has a datatype, and variables can hold values. Python is a powerfully composed language; consequently, we don't have to 
characterize the sort of variable while announcing it. The interpreter binds the value implicitly to its type.


⭐ Standard data types:-
👉 A variable can contain a variety of values. On the other hand, a person's id must be stored as an integer, while their name must be stored 
as a string.
👉 The storage method for each of the standard data types that Python provides is specified by Python. The following is a list of the 
Python-defined data types.


⭐ Types of datatypes
1. Numeric Type:- Integer, float, complex number
2. Sequence Type:- Strings, List, Tuple
3. Boolean:- True, False
4. Set Type:- Set
5. Mapping Type:- Dictionary
6. Binary Data Types:- bytes, bytearray, memory view


Difference Between Mutable and Immutable
✅ Mutable:- A mutable object is one whose value can be changed after it is created.
➤ Examples of Mutable Types: List, Dictionary, Set, bytearray
🔒 Immutable:- An immutable object is one whose value cannot be changed after it is created.
➤ Examples of Immutable Types: Integer, float, Boolean, string, tuple, bytes
"""



#---------------------------------------------------------------------------------------------------------------------
# 1. Numeric:- Integer, float, complex number
a1 = 26                 #integer:- Represents whole numbers without a fractional part.
a2 = 26.5               #float:- Represents real numbers (i.e., numbers with a decimal point).
a3 = complex(3, 5)      #complex:- Represents complex numbers in the form a + bj, where a and b are floats.
print(type(a1))
print(type(a2))
print(type(a3))



#---------------------------------------------------------------------------------------------------------------------
# 2. Sequence Type:- Strings, List, Tuple
b1 = "Hello world"                     #String:- Represents a sequence of Unicode characters (text).
b2 = ["apple", "mango", "banana"]      #List:- An ordered, mutable (changeable) collection of items.
b3 = (1, 2, 3, 4, 5)                   #Tuple:- An ordered, immutable (unchangeable) collection of items.
print(type(b1))
print(type(b2))
print(type(b3))



#---------------------------------------------------------------------------------------------------------------------
# 3. Boolean:- Represents one of two values: True or False.
bool1 = True         #True
bool2 = False        #False
print(type(bool1))



#---------------------------------------------------------------------------------------------------------------------
# 4. Set Type:- Set:- An unordered collection of unique elements.
my_set = {2, 4, 6, 8, "Hello", 23.6}
print(type(my_set))



#---------------------------------------------------------------------------------------------------------------------
# 5. Mapping Type:- Dictionary:- An unordered collection of key-value pairs.
my_dict = {"name":"vikas", "age":28, "city":"Delhi"}
print(type(my_dict))



#---------------------------------------------------------------------------------------------------------------------
# 6. Binary Data Types:- bytes, bytearray, memory view
# 1. bytes:- An immutable sequence of bytes (used for binary data).
byte_data = b"hello"
print(type(byte_data))

# 2. bytearray:- A mutable sequence of bytes.
byte_array = bytearray([65, 66, 67])  # Represents bytes: 'A', 'B', 'C'
print(type(byte_array))

# 3. memory view:- Provides a view object of a bytes-like object without copying the data.
byte_array = bytearray([10, 20, 30, 40, 50])
mem_view = memoryview(byte_array)
print(type(mem_view))



