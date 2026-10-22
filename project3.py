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
        print("student added successfully!")

    elif(enteryourchoice==2):
        for i in students:
            print(f"studentID: {i['studentidentity']} Name: {i['name']} Age: {i['age']} Grade: {i['grade']} | DOB: {i['dob']} | Subjects: {i['subjects']}")  

    elif(enteryourchoice==3):
        enterstudentid = int(input("enter studentid to update: "))
        for i in students:
            if(i["studentidentity"] == enterstudentid):
                print('''
                         1. Update Name
                         2. Update Age
                         3. Update Grade
                         4. Update Subjects
                         ''')
                update=input("what you want to update? : ")
                if update == "1":
                    i['name'] = input("Enter new name: ")
                elif update == "2":
                    i['age'] = int(input("Enter new age: "))
                elif update == "3":
                    i['grade'] = input("Enter new grade: ")
                elif update == "4":
                    subjects = input(" Enter new Subjects (comma-separated): ") 
                    i['subjects'] = set(subjects.split(","))
                else:
                   print("Invalid choice")
                   break
                print("student information updated successfully!")
                break
            else:
                print("student ID not found!")

    elif(enteryourchoice==4):
     studentid=int(input("enter studentid to delete: "))
     for i in students:
        if i["studentidentity"] == studentid:
                students.remove(i)
                print("Student deleted!")
                break
        else:
                print("student not found!")


    elif(enteryourchoice==5):
        for i in students:
         print(f"student id {i['studentidentity']} | Subjects offered: {i['subjects']}")
        
    elif (enteryourchoice==6):
        print("thank you! good bye!")
        break
    else:
        print("invalid choice")





