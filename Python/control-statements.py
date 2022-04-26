#if else
#Print "Hello World" if a is greater than b
# a=int(input("Enter number 1:"))
# b=int(input("Enter number 2:"))
# if a > b:
#     print("Hello world")

#Print "Yes" if a is equal to b, otherwise print "No"
# a=int(input("Enter number 1:"))
# b=int(input("Enter number 2:"))
# if a == b:
#     print("Yes")
# else:
#     print("No")

# Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
# a=int(input("Enter number 1:"))
# b=int(input("Enter number 2:"))
# if a == b:
#     print(1)
# elif a > b:
#     print(2)
# else:
#     print(3)

#While loop
# i=1
# while i <= 6:
#     print(i)
#     i+=1

#for loop
#for loop can itertate through lists and all other built in data tpe to store collection of data ie list, set, tuple and dictionary
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#it can also iterate through a string 
# for x in "banana":
#   print(x)

#for loop using range
# for x in range(6):
#   print(x)
#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
#if given for x in range(a,b) loop will start at a and will go till b

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter
# for x in range(3,30,3):
#     print(x)

#pyramid using for loop
x=5
for i in range(0,x):
    for j in range(0,i+1):
        print("*", end= '') #end='' means that it is a whitespace and dot go to next line
    print("\r")