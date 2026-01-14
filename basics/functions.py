# here we will learn about python functions

# function to calculate mean
# def meanCal(a , b):
#     ans  = (a+b)/2
#     print(ans)

# a  = int(input("Enter value of a: "))
# b =  int(input("Enter value of b: "))

# meanCal(a,b)

arr = [1,2,3,4,5]
x= int(input("X: "))
def   linearSearch(arr , x):
    for i in range(len(arr)):
        if(arr[i] == x):
           
           return i
    return -1
        
ans = linearSearch(arr , x)
if(ans != -1):
    print("element is at index: ",ans)
else:
    print("element not found")