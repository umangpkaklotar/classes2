# first question: concatenation of string
print("=======first question string concatenation=====")

s1= "well"
s2= "done"

print(s1 + s2)

s3 = s1 + " " + s2 # this is output is well done because we added space in between s1 and s2

print(s3)


# string membership operator
print("=======second question string membership operator=====")

greeting = "hello namaste good morning"

print("namaste" in greeting)  # this will return true because namaste is present in greeting

print("hi" in greeting)  # this will return false because hi is not present in greeting

# string partitioning
print("=======third question string partitioning=====") 

sentence = "I am learning  python and java and  programming"

print(sentence.partition("and"))  # this will return a tuple with three elements: the part before the separator, the separator itself, and the part after the separator

print(sentence.count("and"))  # this will return the number of occurrences of the substring "and" in the sentence

# string functions

print("=======forth question string functions=====")

mystr2= " hello world  " 

print(mystr2.count(" ")) # this will return the number of spaces in the string

print(mystr2.strip()) # this will remove the leading and trailing spaces from the string 


prep= " %*  hello world   #@# "

print(prep.strip(" %*#@")) # this will remove the leading and trailing characters specified in the argument from the string

print(prep.count("o")) # this will return the number of occurrences of the character "o" in the string

print(prep.lower()) # this will convert the string to lowercase

print(prep.upper()) # this will convert the string to uppercase  