rows=int(input()) 

for row in range(1,rows):
    
    for j in range(row,0,-1):
        print(j,end= " ")
    print("\r") 
