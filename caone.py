student_record = []
def new_student():
    if len(student_record) > 10 :
        print("student data")
        return
    student = []
    print(" WELCOME TO COLLEGE REGISTRATION ")
    name_student = input("enter name")
    course_name=input("enter course")
    student_num = input("enter num")
    student.append(name_student)
    student.append(course_name)
    student.append(student_num)
    student_record.append(student)
    print("student success")
    return
def display_student():
    index = input("enter index of the array")
    if int(index) > (len(student_record))+1:
        print("student data")
        display_student()
    else:
        print("name " + str(student_record[int(index)][0]))
        print("course" + str(student_record[int(index)][1]))
        print("number" + str(student_record[int(index)][2]))

def delete_student():
    del_index = input("delete student record(enter the index) ")
    del student_record[int(del_index)]
    print("data deleted")

def min_value():
    my_data = student_record
    my_data.sort()
    print(my_data)
    x = min(my_data)
    print(x)

def reenter_student():
  upd_index = input("Enter index  :")
  if int(upd_index) > (len(student_record))+1:
      print("Student data not found!!")
      reenter_student()
  else:
    new_reg = input("Enter new Registration number:")
    new_name = input("Enter new name:")
    new_marks = input("Enter new marks:")
    student_record[int(upd_index)][0] = new_reg
    student_record[int(upd_index)][1] = new_name
    student_record[int(upd_index)][2] = new_marks

    print("Student Data updated successfully")



while True:
    print("Enter 1 to create new Student Record")

    if len(student_record) >= 1:
        print("Enter 2 to Update a student record")

    if len(student_record) >= 1:
        print("Enter 3 to Delete a student record")

    if len(student_record) >= 1:
        print("Enter 4 to Display Student records")

    if len(student_record) >=1:
        print("enter 5 to min value")

    inp = input("Enter your choice")

    if int(inp) == 1:
        new_student()

    elif int(inp) == 2 and len(student_record) >= 1:
        new_student()

    elif int(inp) == 3 and len(student_record) >= 1:
        delete_student()

    elif int(inp) == 4 and len(student_record) >= 1:
        display_student()

    elif int(inp) == 5 and len(student_record) >= 1:
        min_value()


    else:
        print("Invalid Choice, Try again!")