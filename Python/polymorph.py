# polymorphism means the same function name (but different signatures) being used for different types.
# 1)Method overloading: methods can be called using zero or more parameters, this process of calling same method woth different paraams is called method overloading


# class A():
#     def add(self,x=0,y=0,z=0):
#         if(x!=0 and y!= 0 and z!=0):
#             return x+y+z
#     def add(self,x,y,z=0):
#         if(x!=0 and y!= 0):
#             return x+y+z
#     def add(self,x,y=0,z=0):
#         if(x!=0):
#             return x+y+z

# addition=A()
# print(addition.add(1,2,3))
# print(addition.add(1,2))
# print(addition.add(1))

    
# 2)METHOD OVERRIDING
# Ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes
# class Parent(object):
#     def area(self,a,b):
#         print("Area of rectangle: ", a*b)

# class Child(Parent):
#     def area(self,a):
#         super().area(2,2)
#         print("Area of circle: ",3.14*a*a)
# obj=Child()
# print(obj.area(2))

# 3)OPERATOR OVERLOADING:
# Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class.

# Python program to show use of
# + operator for different purposes.
# print(1 + 2)
# # concatenate two strings
# print("Hello "+ "World")
# # Product two numbers
# print(3 * 4)
# # Repeat the String
# print("Hi "*4)

