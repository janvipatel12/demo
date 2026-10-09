for i in range(6):
    for j in range(i):
       print("*" , end="")
    print(" "*(11-i*2),end="")
    for k in range(i):
        print("*" ,end="")
    print()




for i in range(1,5):
    for j in range(1,i+1):
       print("*" , end="")
    for j in range(1,6-i):
        print("?" ,end="")
    print()

