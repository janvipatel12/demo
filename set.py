set1={1,2,3,4,5,6} #mutable
set2=set1.copy() #copy
set3={1,2,3,4,5,6,7,8,9,10}
set1.add(7)
set2.add(8)
print(set1)
print(set1.difference(set2)) #diffrence
set2.difference_update(set1) #diffrence update
print(set1, set2)
set2.discard(10) #remove specific element
print(set2)
print(set1.intersection(set2)) #commom
set1.intersection_update(set2)
print(set1,set2)
print(set1.issubset(set2)) #issubset
print(set2.issuperset(set1)) #issuperset
(set3.remove(8)) #remove element
print(set3)
print(set1.symmetric_difference_update (set3)) #symmetric diffrence
set1.symmetric_difference_update (set3)
print(set1,set3)
print(set1.union(set3))


