'''
lst3=[1,2,3,4,5,66]
for i in lst3:
    print(i**2)


i=0
while(i<len(lst3)):
    print(lst3[i])
    i+=1

for i in range(0,len(lst3)):
    print(lst3[i])    


lstofsquare=[]
for i in range(0,len(lst3)):
    if i%2==0:
         lstofsquare.append((lst3[i]**2)) 
print(lstofsquare)

'''
'''
lst=[1,2,3,4]
lst2=[]
for i in lst:
    lst2.append(i**2)
    print(lst2)


lst2=[i**2 for i in lst2]   
print(lst2) 

lst2=[i for i in lst if i%2==0]
print(lst2) 
'''
lst=[1,2,3,4]
lst2=[]
for i in lst:
    if i%2==0:
        lst2.append("even")
    else:
        lst2.append("odd")
print(lst2)


