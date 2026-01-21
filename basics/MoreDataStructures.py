# sets
# in sets , all element are uniqe
# sets elments are un ordered
# elemets in sets are seprated by commas and are within curly braces

#it can have different data types

# s= {1,2,3,3,4,2,5}
# print(s , type(s))

# for value in s:
#     print(type(value) , value)

# harry = set()
# print(type(harry))

# operations on set
#  1 union op
# s1 = {1,2,3,4}
# s2 = {4,5,6,1}

# # for i in s1.union(s2):
# #     print(i)
# # print(s1.union(s2))

# # intersaction
# for i in s1.intersection(s2):
#     print(i)


#Dictionaries 
# dic are ordered
# dict have key vale pair, seprated by :
# element in dict are seprated by , 

dict ={"Hariom" : "Human" ,
       "Spoon" : "Object",
       1 : 1  
       }
print("print entire dict")
print(dict)
print("Printing just keys of dict")
for key in dict.keys():
    print(dict[key])

print("printing keys values in the dict")
for key , value in dict.items():
    print(f"the value of {key} is {value}")