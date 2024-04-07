print("Data types in Python")

#Integer
num1 = 12
print(num1) 
print(type(num1))

#Float
num2 = 30.65
print(num2)
print(type(num2))

#Complex Numbers
num3 = 12+3j
print(num3)
print(type(num3))

#String
name = "Albert"
print(name)
print(type(name))
print(name[0])
print(name[0:5])
print(name*6)

#Lists
list = ["Hello",6,7,"World",8,"Amen"]
print(list)
print(list[0:4])
list.append("Billionare")

#Tuples
tuple = ("Rere", 3664,2938,"Python","Master")
print(tuple)
print(type(tuple))

#Sets
set1 = {1,3,5,"How,3,43,1,5,3"}
set2 = {1,4,2,3,5,3,"How","Never"}
print(set1)
print(type(set1))
#Both sets
print(set1 | set2)
#Intersection of both sets
print(set1 & set2)
#Difference between two sets
print(set1 - set2)
#Symmetric Difference
print(set1 ^ set2)

#Dictionary
dict1 = {"Name":"Albert","Age":36,"Schools":["Litein","MMU"]}
print(dict1["Name"])
dict1["Name"] = "John"
print(dict1.get("Age"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

name6 = input("Enter your name: ")
print(f"Your Name is :{name6}")