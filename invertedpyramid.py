n=int(input())  
for i in range(0,n): 
    # i+1 is the initial value to print 1 and n+1 is the termination value    
    for j in range(i+1,n+1):
        print("*",end=" ")
    print("\r") #for row

    
