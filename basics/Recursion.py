# Now learning Recursion
# what is Recurion
# Recursion is function which calls itself

#Factorial Function

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return (n*factorial(n-1))
    
print("Factorial of 5: ", factorial(5))