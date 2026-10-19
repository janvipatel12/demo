print("Welcome to the Interactive Personal  Data Collector!")

name=input("enter your name:")
age=int(input("enter your age:"))
height=float(input("enter your height in meters:"))
number=(int(input("enter your favourite number:")))
print (name)
print (age)
print(height)
print(number)

print("Thank you!) Here is the information we collected:")

print("name:", name,
      "(type:", type(name), ",memory address:", id(name),")")
print("age:", age,
      "(type:", type(age), ",memory address:", id(age),")")
print("height:", height,
      "(type:", type(height), ",memory address:", id(height),")")
print("favourite number:", number,
      "(type:", type(number), ",memory address:", id(number),")")

birth_year = 2026 - age

print("your birth year is approximately:", birth_year, "(based on your age of", age, ")")

print("thank you for using the personal data collector. goodbye!")




    

      