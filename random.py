full_name=(input("enter your full name")) 
age=int(input("enter your age"))
salary=int(input("enter your salary"))

print(full_name.strip().title())
print("%s is your name"%(full_name))
print("{0} is your name and {1} is your age and {2} is your salary".format(full_name,age,salary))
print(f"{full_name} is your name and {age} is your age and {salary} is your salary")

