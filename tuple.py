#def same as list
#ordered :  we can update, delete, and access the element
#unmutble(not changable)
#herogenious
#indexing and slicing
#nested tuple
#denoted by ()
# there is only two in-built function: count and index


'''
lst=[1,2,3,4,5,6,7,8] #  sep odd even numbers
lst2=[]
lst3=[]
for i in lst:
    if i%2==0:
        lst2.append(i)
    else:
        lst3.append(i)
print(lst2)
print(lst3)        
'''
lst=[1,2,3,4,5]
revlst=[]


for i in range (len(lst)):
    diglst=lst.pop()
    revlst.append(diglst)
print(revlst)



        
        
