#que 1
lst=[10,20,30,40,50]
for i in lst:
    print(i)

#que 2
lst=[10,20,30]
for i in range(len(lst)):
    print(i,lst[i])

#que 3
lst=[5,10,15,20] 
sum=0
for i in lst: 
    sum=sum+i
    print(sum)

#que 4
lst = [12, 45, 23, 67, 34]
largest = lst[0]
for i in lst:
    if i> largest:
        largest = i
print(largest)

#que 5
lst = [12, 45, 3, 67, 34]
smallest = lst[0]
for i in lst:
    if i < smallest:
        smallest = i
print(smallest)

#que 6
lst = [2, 7, 4, 9, 6, 11]
count = 0
for i in lst:
 if i % 2 == 0:
        count = count + 1
print(count)

#que 7
list = [2, 7, 4, 9, 6, 11]
count = 0
for i in list:
    if i % 2 != 0:
        count = count + 1
print(count)

#que 8
list1 = [10, 15, 22, 31, 44, 51]

for i in list1:
    if i % 2 == 0:
        print(i)

#que 9
list1 = [10, 15, 22, 31, 44, 51]

for i in list1:
    if i % 2 != 0:
        print(i)        

#que 10
list1 = [10, 20, 30, 40]
sum = 0

for i in list1:
    sum = sum + i

average = sum / len(list1)
print(average)


#que 11
list1 = [5, 12, 8, 20, 15, 3]
count = 0

for i in list1:
    if i > 10:
        count = count + 1

print(count)


#que 12
list1 = [5, 12, 8, 20, 15, 3]

for i in list1:
    if i > 10:
        print(i)


#que 13
list1 = [-2, 5, -7, 8, 0, 10]
count = 0

for i in list1:
    if i > 0:
        count = count + 1

print(count)


#que 14
list1 = [-2, 5, -7, 8, 0, -10]
count = 0

for i in list1:
    if i < 0:
        count = count + 1

print(count)


#que 15
list1 = [2, 5, 8, 11, 14]
sum = 0

for i in list1:
    if i % 2 == 0:
        sum = sum + i

print(sum)


#que 16
list1 = [2, 5, 8, 11, 14]
sum = 0

for i in list1:
    if i % 2 != 0:
        sum = sum + i

print(sum)


#que 17
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])


#que 18
list1 = [2, 5, 2, 8, 2, 10]
num = 2
count = 0

for i in list1:
    if i == num:
        count = count + 1

print(count)


#que 19
list1 = [10, 20, 30, 40, 50]
num = 30
found = False

for i in list1:
    if i == num:
        found = True

if found:
    print("Found")
else:
    print("Not Found")


#que 20
list1 = [2, 3, 4, 5]

for i in list1:
    print(i * i)