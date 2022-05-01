#CLASS
# A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods.
# class Human:
#     species="Homo-Sapian"
    
# aaditya=Human()
# print(aaditya.species)

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# class Person:
#   def __init__(self, name, age,gender):
#     self.name = name
#     self.age = age
#     self.gender = gender

# p1 = Person("Aaditya", 36, "Male")
# print(p1.name)
# print(p1.age)
# print(p1.gender)



#Constructor
# class Add:
#     def __init__(self,a,b):
#         print(a+b)

# obj=Add(1,2)
#print(obj)

# class add2():
#     def addition(self,a,b):
#         return a+b
# obj2=add2()
# c=obj2.addition(2,3)
# print(c)

#Inner class:
# create a Color class
# class Color:
	
# # constructor method
# def __init__(self):
# 	# object attributes
# 	self.name = 'Green'
# 	self.lg = self.Lightgreen()
	
# def show(self):
# 	print("Name:", self.name)
	
# create Lightgreen class
# class Lightgreen:
# 	def __init__(self):
# 		self.name = 'Light Green'
# 		self.code = '024avc'
	
# 	def display(self):
# 		print("Name:", self.name)
# 		print("Code:", self.code)

# create Color class object
# outer = Color()

# method calling
# outer.show()

# create a Lightgreen
# inner class object
# g = outer.lg

# inner class method calling
# g.display()

#INHERITANCE
# Inheritance is the capability of one class to derive or inherit the properties from another class. 
# A Python program to demonstrate inheritance

#Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.
# class Person(object):
	
# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name

# 	# To get name
# 	def getName(self):
# 		return self.name

# 	# To check if this person is an employee
# 	def isEmployee(self):
# 		return False


# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):

# 	# Here we return true
# 	def isEmployee(self):
# 		return True

# # Driver code
# emp = Person("Geek1") # An Object of Person
# print(emp.getName(), emp.isEmployee())

# emp = Employee("Geek2") # An Object of Employee
# print(emp.getName(), emp.isEmployee())

#Multiple Inheritance: When a child class inherits from multiple parent classes, it is called multiple inheritance. Unlike java, python shows multiple inheritance
# class Base1(object):
#     def __init__(self):
#         self.str1="Hello"
#         print("Base 1")

# class Base2(object):
#     def __init__(self):
#         self.str2="Hi"
#         print("Base 2")

# class Derived(Base1,Base2):
#     def __init__(self):
#         print("Derived")
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived")

#     def strs(self):
#         print(self.str1, self.str2)

# a=Derived()
# a.strs()

#Multilevel inheritance: When we have a child and grandchild relationship.

# class Base(object):
	
# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name

# 	# To get name
# 	def getName(self):
# 		return self.name


# Inherited or Sub class (Note Person in bracket)
# class Child(Base):
	
# 	# Constructor
# 	def __init__(self, name, age):
# 		Base.__init__(self, name)
# 		self.age = age

# 	# To get name
# 	def getAge(self):
# 		return self.age

# # Inherited or Sub class (Note Person in bracket)
# class GrandChild(Child):
	
# 	# Constructor
# 	def __init__(self, name, age, address):
# 		Child.__init__(self, name, age)
# 		self.address = address

# 	# To get address
# 	def getAddress(self):
# 		return self.address	

# # Driver code
# g = GrandChild("Geek1", 23, "Noida")
# print(g.getName(), g.getAge(), g.getAddress())

# Hierarchical inheritance More than one derived classes are created from a single base