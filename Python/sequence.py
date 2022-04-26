#LISTS
#List is ordered, mutable and allows duplicate elements. Mutable means that the elements in the lists can be change even after defining the list

#A list is created using square brackets[], it allows for different data types and allows duplicate elements
# mylist=["apple", "banana", "cherry"]
# print(mylist)
# mylist2=[1, True, "string", 1]
# print(mylist2)

#We can access indivdual elements of list using index,negative indexing is posssible and -1 index means last element -2 means second last and so on
# item1=mylist[0]
# print(item1)
#we can iterate through whole list using for loop
# for x in mylist:
#     print(x)

#We can check if an element exists in list or not
# if "banana" in mylist:
#     print("Yes element exists")
# else:
#     print("No element does not exist")

#We can get the length of list using len() 
# print(len(mylist))

#we can append elements in the list ie adding new elements at the end of the list using append(element) method
# mylist.append("dates")
# print(mylist)

#we can also insert an element at any position in the list using insert(index, element) method
# mylist.insert(1,"blueberry")
# print(mylist)

#we can remove the last element using pop method
# mylist.pop()
# print(mylist)

#we can also remove a specific element using remove(element) method
# mylist.remove("blueberry")
# print(mylist)

#we can concatanate two lists using + operator
# newlist=mylist + mylist2
# print(newlist)

#slicing a list
# slice=newlist[1:4] #this will slice the list from index 1 to 3. If we dont specify the start index it will start from index 0, similarly if we dont specify end index it will iterate till last element
# print(slice)
# slice=newlist[1:8:2] #the last parameter is the step parameter 
#a simple way to reverse a list without using reverse() method
# reverse=newlist[::-1]
# print(reverse)

#TUPLES
#Tuples are ordered, immutable and allows duplicate elements
#Main difference between tuples and list is that tuples can not be changed after its creation.
#Tuples are created using paranthesis()
# mytuple=("Aaditya", 19, "Male")
# print(mytuple)
#if we define a tuple as mytuple=("Element") and then if we check its type the type will be of string thus single element tuples are defined as mytuple=("tuple", )
#unpacking a tuple
# name, age, gender = mytuple
# print(name)
# print(age)
# print(gender)
#tuple methods are almost similar to list methods


#DICTIONARY
#its an unordered collection of data that is stored in key-value format, it is unordered it is mutable but it does not allow duplicated keys to be stored
#dictionary is created using curly braces{}, and in thode curly braces key-value pair are stored
# mydict={"name":"Aaditya", "age":19, "city":"Mumbai"}
# print(mydict)
# mydict2=dict(name="Roshni", age=19, city="Beed")
# print(mydict2)
#dictionary is mutable thus we can add or change items after creating a dictionary
# mydict["email"]="aaditya@xyzmail.com"
# print(mydict)
#we can remove items using del or pop(key) method popitem() method will remove the last key value pair
# del mydict["email"]
# print(mydict)
# mydict.pop("name")
# print(mydict)


#STRINGS
#String is an array of character it is ordered, immutable and enclosed in "" or '' we can use """ """ for multiline strings
# mystring = "Hello"
# print(mystring)
# char = mystring[0]
# print(char)
# #Concatanating a string
# name = input("Enter your name:")
# greetings= mystring + " " + name
# print(greetings)


#Variables in python
#Method 1: using %s,%d,%f
# var = "Aaditya"
# mystring1 = "The variable is %s" %var
# print(mystring1)
#for integer as a variable we use %d and for float we use %f

#Method 2: using .format() method
# var = "Aaditya"
# var2 = 3.123456
# mystring1 = "The variable is {} and number is {:.4f}".format(var,var2)
# print(mystring1)

#Method 3: f-strings
# var ="Aaditya"
# var2 = 3.123456
# mystring1 = f"The variable is {var} and the number is {var2}"
# print(mystring1)