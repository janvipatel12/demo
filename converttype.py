'''
num="250"
print(int(num)+50)
'''

#implicit  automatic
a=3
b=5
print(a+b)

#explicit
a1="3"
b1="5"
print(a1+b1)
print(type(a1))
print(int(a1)+5)

#to list
print(list("cat")) #string
print(list((4,5,6))) #tuple
print(list(range(3,30))) #range

#to tuple
print(tuple([4,5,3])) #list
print(tuple("name")) #string
tuple(range(5))

#to set
print(set([1,2,3])) #list to set
print(set("hello")) #string to set
frozenset([1,2,3,4,5,5]) #it doesn't change

#dictionary
student = {
    "name": "janvi",
    "age": 21,
    "grade": "A",
    "subject":("hindi", "maths", "english" , "science")
    }
print(student)

