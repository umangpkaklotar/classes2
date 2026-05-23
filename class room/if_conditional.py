# if 
# if else
# if elif else
# nested if  
# what is nested if :- nested if is an if statement that is inside another if statement. It allows you to check multiple conditions and execute different blocks of code based on those conditions.

print("=======first question if statement=====")

a= 10

if(a>5):
    print("a is greater than 5") # this will be executed because the condition is true

# second question if else statement

print("=======second question if else statement=====")

age = int(input("enter your age :- "))

if(age>=18):
    print("you are eligible to vote") # this will be executed if the condition is true
else:
    print("you are not eligible to vote") # this will be executed if the condition is false
    
# third question if elif else statement

print("=======third question if elif else statement=====")  

atm = int(input("enter the amount you want to withdraw :- "))

if(atm>100000):
    print("you can withdraw the amount of 100000") # this will be executed if the condition is true
    
elif(atm>1000):
    print("you can withdraw the amount of 1000") # this will be executed if the condition is true
    
else:
    print("you cannot withdraw the amount ") # this will be executed if the condition is true
    
# fourth question nested if statement

print("=======fourth question nested if statement=====")

num = int(input("enter a number :- "))

if(num<100 and num<200 and num<300 and num<500 and num<1000):
    print("you can withdraw the amount")

elif(num<0):
    print("you cannot withdraw the amount")

else:
    print("something is wrong") 