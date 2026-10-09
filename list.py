#def of list : collection of data types which is used to store multiple elements  in a single variable
#hetrogenous(mixture of many data types)
# ordered: we can access,modify,update,delete element by using index
# mutable; we can make changes in list
# dynamic types 
#noted by [] square braces

# in-built functions

lst=["happy","tanisha","janvi","tanisha","shruti"]
lst2=lst.copy() #copy (make a copy of the list)
print(lst2)

print(lst[1])
print(lst[-2])
lst[3]="aneri" #mutable
print(lst[3])

lst.append("khushi") #append (add one item at the end)
print(lst)

lst.reverse() #reverse (reverse the list)
print(lst)

print(lst2.count("tanisha")) #count (count how many times an item occurs)

lst.extend(["vatsal","meet"]) #extend (add multiple items)
print(lst)

print(lst.index("janvi")) #index (find the position of an item)

lst.insert(1,"tara") #insert (add item at a specific position)
print(lst)

lst.pop(1) #pop (remove an item using position)
print(lst)

lst.remove("janvi") #remove (remove a specific item)
print(lst)

lst.sort() #sort (arrange item in order) (for descending lst.sort(reverse=True))
print(lst)

lst.clear() #clear (remove everything)
print(lst)