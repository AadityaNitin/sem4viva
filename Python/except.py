#Exception are raised when program is syntactically correct but code resuls in error
#Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program.

#ZeroDivisionError:

# a=int(input("Enter number one:"))
# b=int(input("Enter number two:"))
# try:
#     x=a/b
#     print(x)
# except ZeroDivisionError:
#     print("Division by zero is not alllowed")

#NameError
# try:
#     v=a-g
#     print(v)
# except NameError as n:
#     print(n)

#Typeerror:
# a=10
# n="hi"
# try:
#     x=a-n
#     print(x)
# except TypeError as t:
#     print(t)