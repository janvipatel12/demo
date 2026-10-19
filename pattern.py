'''
for i in range(5):
    print("*" , end="")
    for j in range(i):
        print("*" ,end="")
    print()
    '''


'''
for i in range(6):
    for j in range(i):
       print("*" , end="")
    print(" "*(10-i*2),end="")
    for k in range(i):
        print("*" ,end="")
    print()
    '''





'''
for i in range(1,5):
    for j in range(i):
       print("*" , end="")
    for j in range(5-i):
        print("?" ,end="")
    print()
   ''' 


'''
n=5
for i in range(0,n,1):
    for j in range(0,i,1):
      print("*" , end="")
    for z in range(0,(n-i-2)*2+2,1):
      print(" ", end="")
    for j in range(0,i,1):
     print("*" , end="")
    print()
 ''' 
n=5
for i in range(0,5+1,1):
 for j in range(0,5+1,1):
        if(i==0 or i==n or j==0 or j==n):
           print("*", end="")
        else:
           print(" ", end="")
 print()







