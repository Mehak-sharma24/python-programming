
# Project 4: Management System


students = []   # List to store student records


# Mobile Number Verification

def verify_mobile():
    while True:
        mobile = input("Enter your mobile number: ")

        if len(mobile) == 10 and mobile[0] == "9":
            print("Mobile number verified!\n")
            return mobile
        else:
            print("Invalid number! Must be 10 digits and start with 9.\n")



# Add Student (Admin only)

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    students.append({
        "name": name,
        "roll": roll,
        "course": course
    })

    print("Student added successfully!\n")



# Delete Student (Admin only)

def delete_student():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted!\n")
            return

    print("Student not found!\n")



# View All Students (All users)

def view_students():
    if len(students) == 0:
        print("No students available!\n")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Course: {s['course']}")
    print()


# Search Student (Admin + Normal)

def search_student():
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found:")
            print(f"Name: {s['name']}")
            print(f"Roll: {s['roll']}")
            print(f"Course: {s['course']}\n")
            return

    print("Student not found!\n")



# Admin Menu

def admin_menu():
    while True:
        print("----- ADMIN MENU -----")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View Students")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            view_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice!\n")



# Normal User Menu

def normal_menu():
    while True:
        print("----- NORMAL USER MENU -----")
        print("1. View Students")
        print("2. Search Student")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_students()
        elif choice == "2":
            search_student()
        elif choice == "3":
            break
        else:
            print("Invalid choice!\n")



# Guest User Menu

def guest_menu():
    while True:
        print("----- GUEST MENU -----")
        print("1. View Students")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_students()
        elif choice == "2":
            break
        else:
            print("Invalid choice!\n")



# MAIN PROGRAM

print("Welcome to Management System")
verify_mobile()

print("Select User Type:")
print("1. Admin")
print("2. Normal User")
print("3. Guest User")

user_type = input("Enter choice: ")

if user_type == "1":
    admin_menu()
elif user_type == "2":
    normal_menu()
elif user_type == "3":
    guest_menu()
else:
    print("Invalid user type!")