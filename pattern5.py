rows=int(input())
# b is used to contain tha numerical values for this pattern 
for i in range(rows,0,-1): 
    b=i
    for j in range(1,i+1):
        print(b,end= " ") 
    print("\r")
