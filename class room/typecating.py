# what is typecating?Typecasting, also known as type conversion, is the process of converting a value from one data type

# 2 type of type casting in python 

# 1 = autot ypecasting
# 2 =  forced typecasting 

#  firt question: 
print("=======first question typecasting=====")

print(4 + 5.67 + False)

print(4 + 5.6 + False + True)

# second question:
print("=======second question typecasting=====")
print("4" + "5" + "data " + "6.7") # this will concatenate the strings together because they are all strings

# third question: forced typecasting

print("=======third question forced typecasting=====")

a= 9.7 
print(type(a)) # this will return <class 'float'>

print(int(a)) # this will convert the float to  integer by truncating the decimal part, so it will return 9


num = 9

print(type(num)) # this will return <class 'int'>

print(float(num)) # this will convert the integer to float by adding a decimal point, so it will return 9.0

print(str(num)) # this will convert the integer to string, so it will return "9"

print(bool(num)) # this will convert the integer to boolean, so it will return True because any non-zero integer is considered True in Python

print(bool(0)) # this will return False because 0 is considered False in Python

print(bool("")) # this will return False because an empty string is considered False in Python



blank = ""
print(bool(blank)) # this will return False because an empty string is considered False in Python


b= "4"
print(int(b)) # this will convert the string "4" to integer 4

c= int(4.5) +1.2+  int(5.6) + bool(0) # this will raise a ValueError because "4.5" cannot be converted to an integer, and bool(0) will return False which is equivalent to 0 in arithmetic operations.

print(c)
