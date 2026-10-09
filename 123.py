# ouestion: 1,2,3,4
num=1223
num1=num
reversed_num=0
sum=0
count=0
while(num>0):
   dig = num % 10
   sum += dig
   count +=1
   reversed_num = (reversed_num*10)+ dig
   num= num//10
if num1==reversed_num:
    print("palindrome")
else:
    print("not palindrome")  
   
print(reversed_num,sum,count)   
    
"""
num=1223, reversed_num=0, dig=3, reversed_num=(0*10)+3=3, num=122
num=122, reversed_num=3, dig=2, reversed_num=(3*10)+2=32, num=12
num=12, reversed_num=32, dig=2, reversed_num=(32*10)+2=322, num=1
num=1, reversed_num=322, dig=1, reversed_num=(322*10)+1=3221, num=0

"""

# question:6
num=112233112
dig=2
count=0
while(num>0):
   digit=num%10
   if digit==dig:
    count+=1
   num=num//10
print(count)   

"""
digit=2, 2=2, count=1, num=11223311
digit=1, 1!=2,         num=1122331
digit=1, 1!=2,         num=112233
digit=3, 3!=2,         num=11223
digit=3, 3!=2,         num=1122
digit=2, 2=2, count1+1=2, num=112
digit=2, 2=2, count2+1=3, num=11
digit=1, 1!=2,         num=1
digit=1, 1!=2,         num=0

"""

#question:9
num=9875
while(num>=10):
   sum=0
   while(num>0):
      sum+=num%10
      num=num//10
   num=sum
print(num)      
"""

"""
#question:10
n=5
for i in range(1,6):
    for j in range(1, i+1):
        print(j, end="")
    print()