# first question
import sys

print("=====first question===========")
intvar = 10
floatvar = 10.5
strvar = "Hello"    

print(intvar)       
print(floatvar)       
print(strvar)          


# second question 
print("=======second question=====")

species, age, dp = "Dog", 50, 120.4
print("Species:", species)
print("Lifespan in year:", age)
print("Average blood pressure:", dp)

# theird question
print("=======third question=====")
p1= p2= p3= p4= 50

print(p1,p2,p3,p4)

# forth question

print("=======forth question=====")
val2 = 23.4
print(val2)
print(type(val2))
print(sys.getsizeof(val2))
print(val2 ," is a float ? " , isinstance(val2,float))



# fifth question
print("=======fifth question=====")
on= True
off= False

print(isinstance(on,bool))
print(isinstance(off,bool))


print(bool(0))

print(bool(1))


# sixth question
print("=======sixth question=====")
val3= 25 + 3j  # this is complex data type
print(val3)
print(type(val3))   
print(sys.getsizeof(val3))
print(val3 ," is a complex ? " , isinstance(val3,complex))


# seventh question 

print("=======seventh question=====")
str1 = "Hello python"

print(str1[5])

print(str1[-7])

print (len(str1))

str2 = "data is new fuel"

print(str2[0:4])

print(str2[:])

print(str2[6:])

print(str2[-12:-2])

print(str2[::-3])


# eighth question
print("=======eighth question=====")

course= "Python for Data Science"

# print(course[:4])= "Java"

print(course.replace("for","very"))

print(course)

del course #delete the variable course 

# print(course)  this will give error because course variable is deleted     `       `   



