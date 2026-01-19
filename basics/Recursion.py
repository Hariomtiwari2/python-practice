# Now learning Recursion
# what is Recurion
# Recursion is function which calls itself

#Factorial Function

# def factorial(n):
#     if(n == 1 or n == 0):
#         return 1
#     else:
#         return (n*factorial(n-1))
    
# print("Factorial of 5: ", factorial(5))

#Fibonacci series
def fibo(n):
    if(n == 1):
        return 1
    if(n == 0):
        return 0
    
    return (fibo(n-1) + fibo(n-2))
n = int(input("Enter the number: "))
print("Fibonaci of ",n,": " ,fibo(n))