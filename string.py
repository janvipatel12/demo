#def : collection of characters
#ordered
#immutable

sentence=input("enter some sentence")
lstofsen=sentence.split(" ") #convert string into list
lstgt3char=[]
for i in lstofsen:
    if len(i)>3:
        lstgt3char.append(i)
print(lstgt3char)
