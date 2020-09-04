n=int(input())
for i in range(1, n+1):
    #for n no. of spaces
    print(' '*n, end='')
    # for i no. of *
    print('* '*(i))
    # for removing spaces acc to i 
    n-=1
          #  *   
         #  *  *   
         # *  *  *   
        # *  *  *  *   
