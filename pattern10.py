n=int(input())
# for upper triangle
for i in range(n):
    print(' '*(n-i-1)+ '* '*(i+1))
# for lower triangle
for i in range(n-1):
    print(' '*(i+1)+ '* '*(n-i-1))
 
 
# o/p-
#     * 
#    * * 
#   * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
    
    
