print("hello from python + Github")

# if else 
# age = int(input("Enter your age: "))
# if(age > 18):
#     print("Vote")
# elif(age == 18):
#     print("apply for voter id card")
# else:
#     print("you can't vote")

# while loop    
# i=0
# while(i < 10) :
#     if(i % 2 == 0):
#         print(i," is an even number")
#     else:
#         print(i, " is an Odd number")
    
#     i=i+1

# break & Continue  statement
# Break: break statement will end the entire loop if condition met

for i in range(10):
    print(i)
    if(i == 5):
        break

#continue: continue statement skip the particular iteration

for i in range(10):
    if(i==5):
        print("5 will not be printed")
        continue
    print(i)