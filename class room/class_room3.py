# country = input("enter your country name :- ")

# if country.isalpha():

#     if country==country.upper():
#      print("the font entered is in uppercase")
#     elif country==country.lower():
#         print("the font entered is in lowercase")
#     elif country==country.capitalize():
#         print("the font entered is in capitalized")
#     else:
#         print("mixed font is entered")

# else:
#     print("the font entered is not in alphabet")

# print("one of the 4 blocks of code was executed")


# finde larger number among 3 numbers
num1 = int(input("enter the first number:- "))
num2 = int(input("enter the second number:- "))
num3 = int(input("enter the third number:- "))

# all numbers equal
if num1 == num2 and num2 == num3:
    print("all three numbers are equal")

# num1 and num2 equal
elif num1 == num2:

    if num1 > num3:
        print("num1 and num2 are equal and largest :-", num1)

    else:
        print("num1 and num2 are equal but largest number is num3 :-", num3)

# num1 and num3 equal
elif num1 == num3:

    if num1 > num2:
        print("num1 and num3 are equal and largest :-", num1)

    else:
        print("num1 and num3 are equal but largest number is num2 :-", num2)

# num2 and num3 equal
elif num2 == num3:

    if num2 > num1:
        print("num2 and num3 are equal and largest :-", num2)

    else:
        print("num2 and num3 are equal but largest number is num1 :-", num1)

# largest number checking
elif num1 > num2 and num1 > num3:
    print("the largest number is num1 :-", num1)

elif num2 > num1 and num2 > num3:
    print("the largest number is num2 :-", num2)

else:
    print("the largest number is num3 :-", num3)