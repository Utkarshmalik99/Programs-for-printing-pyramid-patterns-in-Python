rows=int(input())
#b is used to contain tha numerical values for this pattern 
b=0 
for i in range(rows,0,-1):
    b=b+1
    for j in range(1,i+1):
        print(b,end= " ") 
    print("\r")
