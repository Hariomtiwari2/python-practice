# here we will learn about python functions

# function to calculate mean
# def meanCal(a , b):
#     ans  = (a+b)/2
#     print(ans)

# a  = int(input("Enter value of a: "))
# b =  int(input("Enter value of b: "))

# meanCal(a,b)

# arr = [1,2,3,4,5]
# x= int(input("X: "))
# def   linearSearch(arr , x):
#     for i in range(len(arr)):
#         if(arr[i] == x):
           
#            return i
#     return -1
        
# ans = linearSearch(arr , x)
# if(ans != -1):
#     print("element is at index: ",ans)
# else:
#     print("element not found")

# function to tell odd or even

# def odd_even( x ):
#     if (x%2 == 0):
#         print("Even number")
#     else:
#         print("Odd number")

# for i in range(1 , 5, 1):
#     x = int(input("Number to check for odd-even: "))
#     print(i,") x: ",x)
#     odd_even(x)


# name function to understand arguments

# def avg(*numbers):
#     print(type(numbers))
#     sum =0
#     for i in numbers:
#         sum = sum + i
#     return sum/len(numbers)  

# # avg(1,2,3,4,5)
# # avg(1,2)
# print(avg(100))

#Exception Handling
# try : try to run a block of code
# Exception : if try block fails to run , run exception block
# finally : this block of code will run irrespective of try or exception 

# try:
#     l = [1,2,4,5]
#     i = int(input("Enter the index: "))
#     print(l[i])
# except Exception as e:
#     print(e)

# finally:
#     ("FINALLY BLOCK WILL ALWAYS BE EXECUTED")

# CUSTOM ERROR
a = int(input("Emter the value b/w 5 and 9: "))
if(a < 5 and a > 9 ):
    raise print( ValueError(("Value should be b/w 5 and 9 !!!!")))