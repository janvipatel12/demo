print("welcome to the student data organizer!")

students=[]
while(True):
    print('''select an option:
          1. select an option
          2. display all students
          3. update student information
          4 .delete student
          5. display subjects offered
          6. exit''') 
    enteryourchoice = int(input("Enter your choice: "))
    if (enteryourchoice==1):
        studentid = int(input("student id: "))
        name = input("name: ")
        age = int(input("age: "))
        grade = input("grade: ")
        dob = input("date of birth (YYYY--MM-DD): ")
        subjects = input("subjects (comma-seprated): ")
        identity_tuple=(studentid,dob)
        studentdic ={
                "studentidentity": studentid,
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subjects": set(subjects.split(","))
            }
        students.append(studentdic)
    elif(enteryourchoice==2):
        for i in students:
            print(f"studentid:{i,studentid}, {i,name}, {i,age}, {i,grade}, {i,dob}, {i,subjects}")    
    elif(enteryourchoice==3):
        enterstudentid = int(input("enter studentid to update: "))
        for i in students:
            if(i["studentidentity"] == enterstudentid):
                enteryourage = input("enter your age: ")
                i["age"] = enteryourage
                enteryourname = input("enter your name: ")
                i["name"]= enteryourname
    elif(enteryourchoice==4):
        studentid=input("enter studentid to delete: ")
        if studentid in students:
            del students[studentid]
            print("student deleted successfully!")
        else:
            print("student not found!")
    elif(enteryourchoice==5):
        for i in students:
         print(i)
        
    elif (enteryourchoice==6):
        print("thank you! good bye!")
        break
    else:
        print("invalid choice")
print(students) 




