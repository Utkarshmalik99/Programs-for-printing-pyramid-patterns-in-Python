num=int(input("Enter the initial no.: "))
rows=int(input("Enter the no. of rows: "))
stop=int(input("Enter the stop value: "))

for row in range(rows):
    
    for j in range(1,stop):
        print(num,end= " ")
        num+=1
    print("\r")
    stop+=1


# 1 
# 2 3 
# 4 5 6  
# 7 8 9 10
