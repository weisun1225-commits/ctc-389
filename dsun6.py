#Dawei Sun
#CTC 389
#8-27-26

students = ["Benjamin", "Alison", "Brianna", "Catherine", "Phoenix"]

print("1 Add student to list")
print("2 Modify student name")
print("3 Remove student")

choice = int(input("Choose an option: "))

if choice == 1:
    newName = input("Enter a student name: ")

    students.append(newName)

    print("New student list:")
    for i in students:
        print(i)

elif choice == 2:
    for i in range(5):
        print(i, students[i])

    studentNumber = int(input("Enter the index number to change: "))
    newName = input("Enter a new student name: ")

    students[studentNumber] = newName

    print("New student list:")
    for i in students:
        print(i)

elif choice == 3:
    for i in range(5):
        print(i, students[i])

    studentNumber = int(input("Enter the index number to remove: "))

    students.pop(studentNumber)

    print("New student list:")
    for i in students:
        print(i)





