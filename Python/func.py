#Python Functions is a block of related statements designed to perform a computational, logical, or evaluative task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again

#Creating a function: We use def() keyword to create a function
# def greetings(name):
#     print("Hello " + name)

# greetings("Aaditya")

#We can pass default arguments also
# def myfunc(x, y=50):
#     print("x:", x)
#     print("y:", y)

# myfunc(10)

#return statements
# def sqr(num):
#     return num**2
# print(sqr(2))
# print(sqr(-4))

#Annonymous/lambda function
#Anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions

#Python Lambda Function Syntax:

#lambda arguments: expression
# def cube(y):
    # return y*y*y
# lambda_cube = lambda y: y*y*y
 
# using the normally
# defined function
# print(cube(5))
 
# using the lambda function
# print(lambda_cube(5))
# Max = lambda a, b : a if(a > b) else b
# print(Max(1, 2))

# filter() with lambda()
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(filter(lambda x: (x%2 != 0) , li))
# print(final_list)

# Python 3 code to people above 18 yrs
# ages = [13, 90, 17, 59, 21, 60, 5]
# adults = list(filter(lambda age: age>18, ages))
# print(adults)

# map() with lambda()
# to get double of a list.
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(map(lambda x: x*2, li))
# print(final_list)


# animals = ['dog', 'cat', 'parrot', 'rabbit']
# here we intend to change all animal names
# to upper case and return the same
# uppered_animals = list(map(lambda animal: str.upper(animal), animals))
# print(uppered_animals)

# reduce() function in Python takes in a function and a list as an argument. The function is called with a lambda function and an iterable and a new reduced result is returned. This performs a repetitive operation over the pairs of the iterable. The reduce() function belongs to the  functools module.

# reduce() with lambda()
# to get sum of a list
 
# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print (sum)


#maximum in a list using reduce()
# import functools
# initializing list
# lis = [ 1 , 3, 5, 6, 2, ]
# using reduce to compute maximum element from list
# print ("The maximum element of the list is : ",end="")
# print (functools.reduce(lambda a,b : a if a > b else b,lis))