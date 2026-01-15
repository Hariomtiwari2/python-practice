# list data structure
# list of 1st 10 even numbers
even = []
i=1
while(i<40):
    if(i%2 == 0):
        even.append(i)
    i= i+1

    if(len(even) == 10):
        break

# print(even)
x=0
for i in range(1 , 11 ,1):
    print(i , " ",even[x])
    x = x+1

even.append(100)
